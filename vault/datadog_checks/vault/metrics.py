# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
METRIC_MAP = {
    'go_gc_duration_seconds': 'go.gc.duration.seconds',
    'go_goroutines': 'go.goroutines',
    'go_info': 'go.info',
    'go_memstats_alloc_bytes': 'go.memstats.alloc.bytes',
    'go_memstats_alloc_bytes_total': 'go.memstats.alloc.bytes.total',
    'go_memstats_buck_hash_sys_bytes': 'go.memstats.buck_hash.sys.bytes',
    'go_memstats_frees_total': 'go.memstats.frees.total',
    'go_memstats_gc_cpu_fraction': 'go.memstats.gc.cpu.fraction',
    'go_memstats_gc_sys_bytes': 'go.memstats.gc.sys.bytes',
    'go_memstats_heap_alloc_bytes': 'go.memstats.heap.alloc.bytes',
    'go_memstats_heap_idle_bytes': 'go.memstats.heap.idle.bytes',
    'go_memstats_heap_inuse_bytes': 'go.memstats.heap.inuse.bytes',
    'go_memstats_heap_objects': 'go.memstats.heap.objects',
    'go_memstats_heap_released_bytes': 'go.memstats.heap.released.bytes',
    'go_memstats_heap_sys_bytes': 'go.memstats.heap.sys.bytes',
    'go_memstats_last_gc_time_seconds': 'go.memstats.last.gc.time.seconds',
    'go_memstats_lookups_total': 'go.memstats.lookups.total',
    'go_memstats_mallocs_total': 'go.memstats.mallocs.total',
    'go_memstats_mcache_inuse_bytes': 'go.memstats.mcache.inuse.bytes',
    'go_memstats_mcache_sys_bytes': 'go.memstats.mcache.sys.bytes',
    'go_memstats_mspan_inuse_bytes': 'go.memstats.mspan.inuse.bytes',
    'go_memstats_mspan_sys_bytes': 'go.memstats.mspan.sys.bytes',
    'go_memstats_next_gc_bytes': 'go.memstats.next.gc.bytes',
    'go_memstats_other_sys_bytes': 'go.memstats.other.sys.bytes',
    'go_memstats_stack_inuse_bytes': 'go.memstats.stack.inuse.bytes',
    'go_memstats_stack_sys_bytes': 'go.memstats.stack.sys.bytes',
    'go_memstats_sys_bytes': 'go.memstats.sys.bytes',
    'go_threads': 'go.threads',
    'process_cpu_seconds_total': 'process.cpu.seconds.total',
    'process_max_fds': 'process.max.fds',
    'process_open_fds': 'process.open.fds',
    'process_resident_memory_bytes': 'process.resident_memory.bytes',
    'process_start_time_seconds': 'process.start_time.seconds',
    'process_virtual_memory_bytes': 'process.virtual_memory.bytes',
    'process_virtual_memory_max_bytes': 'process.virtual_memory.max.bytes',
    'vault_audit_log_request': 'vault.audit.log.request',
    'vault_audit_log_response': 'vault.audit.log.response',
    'vault_audit_log_request_failure': 'vault.audit.log.request.failure',
    'vault_audit_log_response_failure': 'vault.audit.log.response.failure',
    'vault_barrier_delete': 'vault.barrier.delete',
    'vault_barrier_get': 'vault.barrier.get',
    'vault_barrier_put': 'vault.barrier.put',
    'vault_barrier_list': 'vault.barrier.list',
    'vault_cache_hit': 'vault.cache.hit',
    'vault_cache_miss': 'vault.cache.miss',
    'vault_cache_write': 'vault.cache.write',
    'vault_cache_delete': 'vault.cache.delete',
    'vault_core_check_token': 'vault.core.check.token',
    'vault_core_fetch_acl_and_token': 'vault.core.fetch.acl_and_token',
    'vault_core_handle_request': 'vault.core.handle.request',
    'vault_core_handle_login_request': 'vault.core.handle.login_request',
    'vault_core_leadership_setup_failed': 'vault.core.leadership.setup_failed',
    'vault_core_leadership_lost': 'vault.core.leadership.lost',
    'vault_core_post_unseal': 'vault.core.post_unseal',
    'vault_core_pre_seal': 'vault.core.pre_seal',
    'vault_core_seal_with_request': 'vault.core.seal_with_request',
    'vault_core_seal': 'vault.core.seal',
    'vault_core_seal_internal': 'vault.core.seal_internal',
    'vault_core_step_down': 'vault.core.step_down',
    'vault_core_unseal': 'vault.core.unseal',
    'vault_expire_fetch_lease_times': 'vault.expire.fetch.lease.times',
    'vault_expire_fetch_lease_times_by_token': 'vault.expire.fetch.lease.times.by_token',
    'vault_expire_num_leases': 'vault.expire.num_leases',
    'vault_expire_leases_by_expiration': 'vault.expire.leases.by_expiration',
    'vault_expire_lease_expiration': 'vault.expire.lease_expiration',
    'vault_expire_job_manager_total_jobs': 'vault.expire.job_manager.total_jobs',
    'vault_expire_job_manager_queue_length': 'vault.expire.job_manager.queue_length',
    'vault_expire_lease_expiration_time_in_queue': 'vault.expire.lease_expiration.time_in_queue',
    'vault_expire_lease_expiration_error': 'vault.expire.lease_expiration.error',
    'vault_expire_revoke': 'vault.expire.revoke',
    'vault_expire_revoke_force': 'vault.expire.revoke.force',
    'vault_expire_revoke_prefix': 'vault.expire.revoke.prefix',
    'vault_expire_revoke_by_token': 'vault.expire.revoke.by_token',
    'vault_expire_renew': 'vault.expire.renew',
    'vault_expire_renew_token': 'vault.expire.renew_token',
    'vault_expire_register': 'vault.expire.register',
    'vault_expire_register_auth': 'vault.expire.register.auth',
    'vault_policy_get_policy': 'vault.policy.get_policy',
    'vault_policy_list_policies': 'vault.policy.list_policies',
    'vault_policy_delete_policy': 'vault.policy.delete_policy',
    'vault_policy_set_policy': 'vault.policy.set_policy',
    'vault_token_create': 'vault.token.create',
    'vault_token_createAccessor': 'vault.token.createAccessor',
    'vault_token_lookup': 'vault.token.lookup',
    'vault_token_revoke': 'vault.token.revoke',
    'vault_token_revoke_tree': 'vault.token.revoke.tree',
    'vault_token_store': 'vault.token.store',
    'vault_quota_rate_limit_violation': 'vault.quota.rate_limit.violation',
    'vault_quota_lease_count_violation': 'vault.quota.lease_count.violation',
    'vault_rollback_attempt_auth_jwt_': 'vault.rollback.attempt.auth.jwt',
    'vault_rollback_attempt_auth_ldap_': 'vault.rollback.attempt.auth.ldap',
    'vault_rollback_attempt_secret_': 'vault.rollback.attempt.secret',
    'vault_rollback_attempt_auth_token_': 'vault.rollback.attempt.auth.token',
    'vault_rollback_attempt_cubbyhole_': 'vault.rollback.attempt.cubbyhole',
    'vault_rollback_attempt_identity_': 'vault.rollback.attempt.identity',
    'vault_rollback_attempt_sys_': 'vault.rollback.attempt.sys',
    'vault_runtime_alloc_bytes': 'vault.runtime.alloc.bytes',
    'vault_runtime_free_count': 'vault.runtime.free.count',
    'vault_runtime_heap_objects': 'vault.runtime.heap.objects',
    'vault_runtime_malloc_count': 'vault.runtime.malloc.count',
    'vault_runtime_num_goroutines': 'vault.runtime.num_goroutines',
    'vault_runtime_sys_bytes': 'vault.runtime.sys.bytes',
    'vault_runtime_total_gc_pause_ns': 'vault.runtime.total.gc.pause_ns',
    'vault_runtime_gc_pause_ns': 'vault.runtime.gc.pause_ns',
    'vault_runtime_total_gc_runs': 'vault.runtime.total.gc.runs',
    'vault_merkle_flushDirty': 'vault.merkle.flushdirty',
    'vault_merkle_saveCheckpoint': 'vault.merkle.savecheckpoint',
    'vault_wal_deleteWALs': 'vault.wal.deletewals',
    'vault_wal_gc_deleted': 'vault.wal.gc.deleted',
    'vault_wal_gc_total': 'vault.wal.gc.total',
    'vault_wal_loadWAL': 'vault.wal.loadWAL',
    'vault_wal_persistWALs': 'vault.wal.persistwals',
    'vault_wal_flushReady': 'vault.wal.flushready',
    'vault_logshipper_streamWALs_missing_guard': 'logshipper.streamWALs.missing_guard',
    'vault_logshipper_streamWALs_guard_found': 'logshipper.streamWALs.guard_found',
    'vault_replication_fetchRemoteKeys': 'replication.fetchRemoteKeys',
    'vault_replication_merkleDiff': 'replication.merkleDiff',
    'vault_replication_merkleSync': 'replication.merkleSync',
    'vault_replication_merkle_commit_index': 'replication.merkle.commit_index',
    'vault_replication_wal_gc': 'replication.wal.gc',
    'vault_replication_wal_last_wal': 'replication.wal.last_wal',
    'vault_replication_wal_last_dr_wal': 'replication.wal.last_dr_wal',
    'vault_replication_wal_last_performance_wal': 'replication.wal.last_performance_wal',
    'vault_replication_fsm_last_remote_wal': 'replication.fsm.last_remote_wal',
    'vault_replication_rpc_server_auth_request': 'replication.rpc.server.auth_request',
    'vault_replication_rpc_server_bootstrap_request': 'replication.rpc.server.bootstrap_request',
    'vault_replication_rpc_server_conflicting_pages_request': 'replication.rpc.server.conflicting_pages_request',
    'vault_replication_rpc_server_echo': 'replication.rpc.server.echo',
    'vault_replication_rpc_server_forwarding_request': 'replication.rpc.server.forwarding_request',
    'vault_replication_rpc_server_guard_hash_request': 'replication.rpc.server.guard_hash_request',
    'vault_replication_rpc_server_persist_alias_request': 'replication.rpc.server.persist_alias_request',
    'vault_replication_rpc_server_persist_persona_request': 'replication.rpc.server.persist_persona_request',
    'vault_replication_rpc_server_stream_wals_request': 'replication.rpc.server.stream_wals_request',
    'vault_replication_rpc_server_sub_page_hashes_request': 'replication.rpc.server.sub_page_hashes_request',
    'vault_replication_rpc_server_sync_counter_request': 'replication.rpc.server.sync_counter_request',
    'vault_replication_rpc_server_upsert_group_request': 'replication.rpc.server.upsert_group_request',
    'vault_replication_rpc_client_conflicting_pages': 'replication.rpc.client.conflicting_pages',
    'vault_replication_rpc_client_fetch_keys': 'replication.rpc.client.fetch_keys',
    'vault_replication_rpc_client_forward': 'replication.rpc.client.forward',
    'vault_replication_rpc_client_guard_hash': 'replication.rpc.client.guard_hash',
    'vault_replication_rpc_client_persist_alias': 'replication.rpc.client.persist_alias',
    'vault_replication_rpc_client_register_auth': 'replication.rpc.client.register_auth',
    'vault_replication_rpc_client_register_lease': 'replication.rpc.client.register_lease',
    'vault_replication_rpc_client_stream_wals': 'replication.rpc.client.stream_wals',
    'vault_replication_rpc_client_sub_page_hashes': 'replication.rpc.client.sub_page_hashes',
    'vault_replication_rpc_client_sync_counter': 'replication.rpc.client.sync_counter',
    'vault_replication_rpc_client_upsert_group': 'replication.rpc.client.upsert_group',
    'vault_replication_rpc_client_wrap_in_cubbyhole': 'replication.rpc.client.wrap_in_cubbyhole',
    'vault_replication_rpc_dr_server_echo': 'replication.rpc.dr.server.echo',
    'vault_replication_rpc_dr_server_fetch_keys_request': 'replication.rpc.dr.server.fetch_keys_request',
    'vault_replication_rpc_standby_server_echo': 'replication.rpc.standby.server.echo',
    'vault_replication_rpc_standby_server_register_auth_request': (
        'replication.rpc.standby.server.register_auth_request'
    ),
    'vault_replication_rpc_standby_server_register_lease_request': (
        'replication.rpc.standby.server.register_lease_request'
    ),
    'vault_replication_rpc_standby_server_wrap_token_request': 'replication.rpc.standby.server.wrap_token_request',
    'vault_database_Initialize': 'database.Initialize',
    'vault_database_Initialize_error': 'database.Initialize.error',
    'vault_database_Close': 'database.Close',
    'vault_database_Close_error': 'database.Close.error',
    'vault_database_CreateUser': 'database.CreateUser',
    'vault_database_CreateUser_error': 'database.CreateUser.error',
    'vault_database_RenewUser': 'database.RenewUser',
    'vault_database_RenewUser_error': 'database.RenewUser.error',
    'vault_database_RevokeUser': 'database.RevokeUser',
    'vault_database_RevokeUser_error': 'database.RevokeUser.error',
    'vault_azure_put': 'vault.azure.put',
    'vault_azure_get': 'vault.azure.get',
    'vault_azure_delete': 'vault.azure.delete',
    'vault_azure_list': 'vault.azure.list',
    'vault_cassandra_put': 'vault.cassandra.put',
    'vault_cassandra_get': 'vault.cassandra.get',
    'vault_cassandra_delete': 'vault.cassandra.delete',
    'vault_cassandra_list': 'vault.cassandra.list',
    'vault_cockroachdb_put': 'vault.cockroachdb.put',
    'vault_cockroachdb_get': 'vault.cockroachdb.get',
    'vault_cockroachdb_delete': 'vault.cockroachdb.delete',
    'vault_cockroachdb_list': 'vault.cockroachdb.list',
    'vault_consul_put': 'vault.consul.put',
    'vault_consul_get': 'vault.consul.get',
    'vault_consul_delete': 'vault.consul.delete',
    'vault_consul_list': 'vault.consul.list',
    'vault_couchdb_put': 'vault.couchdb.put',
    'vault_couchdb_get': 'vault.couchdb.get',
    'vault_couchdb_delete': 'vault.couchdb.delete',
    'vault_couchdb_list': 'vault.couchdb.list',
    'vault_dynamodb_put': 'vault.dynamodb.put',
    'vault_dynamodb_get': 'vault.dynamodb.get',
    'vault_dynamodb_delete': 'vault.dynamodb.delete',
    'vault_dynamodb_list': 'vault.dynamodb.list',
    'vault_etcd_put': 'vault.etcd.put',
    'vault_etcd_get': 'vault.etcd.get',
    'vault_etcd_delete': 'vault.etcd.delete',
    'vault_etcd_list': 'vault.etcd.list',
    'vault_gcs_put': 'vault.gcs.put',
    'vault_gcs_get': 'vault.gcs.get',
    'vault_gcs_delete': 'vault.gcs.delete',
    'vault_gcs_list': 'vault.gcs.list',
    'vault_gcs_lock_unlock': 'vault.gcs.lock.unlock',
    'vault_gcs_lock_lock': 'vault.gcs.lock.lock',
    'vault_gcs_lock_value': 'vault.gcs.lock.value',
    'vault_identity_entity_count': 'vault.identity.entity.count',
    'vault_identity_entity_creation': 'vault.identity.entity.creation',
    'vault_identity_entity_alias_count': 'vault.identity.entity.alias.count',
    'vault_mssql_put': 'vault.mssql.put',
    'vault_mssql_get': 'vault.mssql.get',
    'vault_mssql_delete': 'vault.mssql.delete',
    'vault_mssql_list': 'vault.mssql.list',
    'vault_mysql_put': 'vault.mysql.put',
    'vault_mysql_get': 'vault.mysql.get',
    'vault_mysql_delete': 'vault.mysql.delete',
    'vault_mysql_list': 'vault.mysql.list',
    'vault_postgres_put': 'vault.postgres.put',
    'vault_postgres_get': 'vault.postgres.get',
    'vault_postgres_delete': 'vault.postgres.delete',
    'vault_postgres_list': 'vault.postgres.list',
    'vault_raft_put': 'vault.raft.put',
    'vault_raft_get': 'vault.raft.get',
    'vault_raft_delete': 'vault.raft.delete',
    'vault_raft_list': 'vault.raft.list',
    'vault_raft_storage_put': 'vault.raft_storage.put',
    'vault_raft_storage_get': 'vault.raft_storage.get',
    'vault_raft_storage_delete': 'vault.raft_storage.delete',
    'vault_raft_storage_list': 'vault.raft_storage.list',
    'vault_raft_leader_lastContact': 'vault.raft.leader.lastContact',
    'vault_raft_state_candidate': 'vault.raft.state.candidate',
    'vault_raft_state_leader': 'vault.raft.state.leader',
    'vault_s3_put': 'vault.s3.put',
    'vault_s3_get': 'vault.s3.get',
    'vault_s3_delete': 'vault.s3.delete',
    'vault_s3_list': 'vault.s3.list',
    'vault_token_count': 'vault.token.count',
    'vault_token_count_by_auth': 'vault.token.count.by_auth',
    'vault_token_count_by_policy': 'vault.token.count.by_policy',
    'vault_token_count_by_ttl': 'vault.token.count.by_ttl',
    'vault_token_creation': 'vault.token.creation',
    'vault_secret_kv_count': 'vault.secret.kv.count',
    'vault_secret_lease_creation': 'vault.secret.lease.creation',
    'vault_spanner_put': 'vault.spanner.put',
    'vault_spanner_get': 'vault.spanner.get',
    'vault_spanner_delete': 'vault.spanner.delete',
    'vault_spanner_list': 'vault.spanner.list',
    'vault_spanner_lock_unlock': 'vault.spanner.lock.unlock',
    'vault_spanner_lock_lock': 'vault.spanner.lock.lock',
    'vault_spanner_lock_value': 'vault.spanner.lock.value',
    'vault_swift_put': 'vault.swift.put',
    'vault_swift_get': 'vault.swift.get',
    'vault_swift_delete': 'vault.swift.delete',
    'vault_swift_list': 'vault.swift.list',
    'vault_zookeeper_put': 'vault.zookeeper.put',
    'vault_zookeeper_get': 'vault.zookeeper.get',
    'vault_zookeeper_delete': 'vault.zookeeper.delete',
    'vault_zookeeper_list': 'vault.zookeeper.list',
}

METRIC_ROLLBACK_COMPAT_MAP = {
    'vault_route_rollback_auth_jwt_': 'vault.route.rollback.auth.jwt',
    'vault_route_rollback_auth_ldap_': 'vault.route.rollback.auth.ldap',
    'vault_route_rollback_auth_token_': 'vault.route.rollback.auth.token',
    'vault_route_rollback_cubbyhole_': 'vault.route.rollback.cubbyhole',
    'vault_route_rollback_identity_': 'vault.route.rollback.identity',
    'vault_route_rollback_sys_': 'vault.route.rollback.sys',
    'vault_route_rollback_secret_': 'vault.route.rollback.secret',
}

ROUTE_METRICS_TO_TRANSFORM = [
    'vault_route_create_',
    'vault_route_delete_',
    'vault_route_list_',
    'vault_route_read_',
    'vault_route_rollback_',
]

KNOWN_GAUGES = {'vault_runtime_free_count', 'vault_runtime_malloc_count', 'vault_wal_gc_total'}


def construct_metrics_config(metric_map, type_overrides):
    dynamic_metrics = {'go_memstats_alloc_bytes', 'go_memstats_alloc_bytes_total'}
    metrics = []
    for raw_metric_name, metric_name in metric_map.items():
        if raw_metric_name in dynamic_metrics:
            continue
        elif raw_metric_name.endswith('_total') and raw_metric_name not in KNOWN_GAUGES:
            raw_metric_name = raw_metric_name[:-6]
            metric_name = metric_name[:-6]
        elif metric_name.endswith('.count') and raw_metric_name not in KNOWN_GAUGES:
            metric_name = metric_name[:-6]

        config = {raw_metric_name: {'name': metric_name}}
        if raw_metric_name in type_overrides:
            config[raw_metric_name]['type'] = type_overrides[raw_metric_name]

        metrics.append(config)

    metrics.append({'go_memstats_alloc_bytes': {'name': 'go.memstats.alloc.bytes', 'type': 'native_dynamic'}})

    return metrics
