from cloudify import ctx

ctx.logger.info('CPE updating: {}'.format(str(ctx.instance.runtime_properties)))
