# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from typing import Any

import mock
import pytest
from packaging import version

from datadog_checks.base.stubs.aggregator import AggregatorStub
from datadog_checks.marklogic import MarklogicCheck

from .common import INSTANCE, INSTANCE_FILTERS, MARKLOGIC_VERSION
from .metrics import (
    FOREST_STATUS_SUMMARY_METRICS,
    GLOBAL_METRICS,
    HOST_STATUS_METRICS,
    REQUESTS_STATUS_METRICS,
    RESOURCE_STORAGE_FOREST_METRICS,
    SERVER_STATUS_METRICS,
    STORAGE_FOREST_METRICS,
    STORAGE_HOST_METRICS,
    TRANSACTION_STATUS_METRICS,
)


@pytest.mark.integration
@pytest.mark.usefixtures("dd_environment")
def test_check(aggregator):
    # type: (AggregatorStub) -> None
    check = MarklogicCheck('marklogic', {}, [INSTANCE])

    check.check(INSTANCE)

    tags = ['foo:bar']

    for metric in GLOBAL_METRICS:
        aggregator.assert_metric(metric, tags=tags)

    storage_tag_prefixes = ['storage_path', 'host_name', 'host_id']
    for metric in STORAGE_HOST_METRICS:
        for tag in tags:
            aggregator.assert_metric_has_tag(metric, tag)
        for prefix in storage_tag_prefixes:
            aggregator.assert_metric_has_tag_prefix(metric, prefix)
    for metric in STORAGE_FOREST_METRICS:
        for tag in tags:
            aggregator.assert_metric_has_tag(metric, tag)
        for prefix in storage_tag_prefixes + ['forest_id', 'forest_name']:
            aggregator.assert_metric_has_tag_prefix(metric, prefix)

    aggregator.assert_all_metrics_covered()


@pytest.mark.integration
@pytest.mark.usefixtures("dd_environment")
def test_check_with_filters(aggregator):
    # type: (AggregatorStub) -> None
    check = MarklogicCheck('marklogic', {}, [INSTANCE_FILTERS])

    check.check(INSTANCE_FILTERS)

    for metric in HOST_STATUS_METRICS + SERVER_STATUS_METRICS + TRANSACTION_STATUS_METRICS:
        aggregator.assert_metric(metric, count=1)
    for metric in FOREST_STATUS_SUMMARY_METRICS + REQUESTS_STATUS_METRICS:
        aggregator.assert_metric(metric, at_least=1)
    for metric in STORAGE_HOST_METRICS:
        aggregator.assert_metric(metric, count=2)
        aggregator.assert_metric_has_tag(metric, 'forest_name:Security', count=1)
    for metric in STORAGE_FOREST_METRICS:
        aggregator.assert_metric(metric, count=10)

    # Resource filter only
    for metric in RESOURCE_STORAGE_FOREST_METRICS:
        aggregator.assert_metric(metric, tags=['forest_name:Security'], count=1)
    for metric in [
        'marklogic.requests.query-count',
        'marklogic.requests.total-requests',
        'marklogic.requests.update-count',
    ]:
        aggregator.assert_metric(metric, tags=['server_name:Admin', 'group_name:Default'], count=1)

    aggregator.assert_all_metrics_covered()

    # Service checks
    aggregator.assert_service_check('marklogic.can_connect', MarklogicCheck.OK, count=1)
    aggregator.assert_service_check('marklogic.database.health', MarklogicCheck.OK, count=10)


@pytest.mark.integration
@pytest.mark.usefixtures('dd_environment')
def test_metadata_integration(aggregator, datadog_agent):
    # type: (AggregatorStub, Any) -> None
    c = MarklogicCheck('marklogic', {}, [INSTANCE])
    c.check_id = 'test:123'
    c.check(INSTANCE)

    parsed_version = version.parse(MARKLOGIC_VERSION)
    version_metadata = {
        'version.scheme': 'marklogic',
        'version.major': str(parsed_version.major),
        'version.minor': str(parsed_version.minor),
        'version.patch': str(parsed_version.post),
        'version.raw': MARKLOGIC_VERSION,
    }

    datadog_agent.assert_metadata('test:123', version_metadata)
    datadog_agent.assert_metadata_count(len(version_metadata))

    # Service checks
    aggregator.assert_service_check('marklogic.can_connect', MarklogicCheck.OK, count=1)
    aggregator.assert_service_check('marklogic.database.health', MarklogicCheck.OK, count=10)
    aggregator.assert_service_check('marklogic.forest.health', MarklogicCheck.OK, count=10)


@pytest.mark.e2e
def test_e2e(dd_agent_check):
    # type: (Any) -> None
    aggregator = dd_agent_check(INSTANCE, rate=True)

    for metric in GLOBAL_METRICS:
        aggregator.assert_metric(metric, count=2)
    for metric in STORAGE_HOST_METRICS:
        aggregator.assert_metric(metric, count=2)
    for metric in STORAGE_FOREST_METRICS:
        aggregator.assert_metric(metric, count=20)

    aggregator.assert_all_metrics_covered()

    # Service checks
    aggregator.assert_service_check('marklogic.can_connect', MarklogicCheck.OK, count=2)
    aggregator.assert_service_check('marklogic.database.health', MarklogicCheck.OK, count=20)
    aggregator.assert_service_check('marklogic.forest.health', MarklogicCheck.OK, count=20)


def test_submit_health_service_checks(aggregator, caplog):
    # type: (AggregatorStub, Any) -> None
    check = MarklogicCheck('marklogic', {}, [INSTANCE])

    health_mocked_data = {
        'cluster-health-report': [
            {
                "state": "info",
                "resource-type": "database",
                "resource-name": "Security",
                "code": "HEALTH-DATABASE-NO-BACKUP",
                "message": "Database has never been backed up.",
            },
            {'resource-type': 'database', 'resource-name': 'Fab', 'code': 'UNKNOWN'},
        ]
    }

    check.resources = [
        {'id': '255818103205892753', 'type': 'database', 'name': 'Security', 'uri': "/databases/Security"},
        {'id': '5004266825873163057', 'type': 'database', 'name': 'Fab', 'uri': "/databases/Fab"},
        {'id': '16024526243775340149', 'type': 'forest', 'name': 'Modules', 'uri': "/forests/Modules"},
        {'id': '17254568917360711355', 'type': 'forest', 'name': 'Extensions', 'uri': "/forests/Extensions"},
    ]

    # If there is no error
    with mock.patch('datadog_checks.marklogic.api.MarkLogicApi.get_health', return_value=health_mocked_data):
        check.submit_health_service_checks()

        aggregator.assert_service_check(
            'marklogic.database.health',
            MarklogicCheck.OK,
            tags=['foo:bar', 'database_name:Security'],
            message='HEALTH-DATABASE-NO-BACKUP (info): Database has never been backed up.',
            count=1,
        )
        aggregator.assert_service_check(
            'marklogic.database.health',
            MarklogicCheck.UNKNOWN,
            tags=['foo:bar', 'database_name:Fab'],
            message='UNKNOWN (unknown): No message.',
            count=1,
        )
        aggregator.assert_service_check(
            'marklogic.forest.health', MarklogicCheck.OK, tags=['foo:bar', 'forest_name:Modules'], message=None, count=1
        )
        aggregator.assert_service_check(
            'marklogic.forest.health',
            MarklogicCheck.OK,
            tags=['foo:bar', 'forest_name:Extensions'],
            message=None,
            count=1,
        )

    aggregator.reset()
    caplog.clear()

    # If the user doesn't have enough permissions
    with mock.patch(
        'datadog_checks.marklogic.api.MarkLogicApi.get_health', return_value={'code': 'HEALTH-CLUSTER-ERROR'}
    ):
        check.submit_health_service_checks()

        assert "The user needs `manage-admin` permission to monitor databases health." in caplog.text

    aggregator.reset()
    caplog.clear()

    # If MarkLogic can't be reached
    with mock.patch('datadog_checks.marklogic.api.MarkLogicApi.get_health', side_effect=Exception("exception")):
        check.submit_health_service_checks()

        assert "Failed to monitor databases health" in caplog.text
