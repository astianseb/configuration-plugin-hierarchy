from cloudify import ctx

ctx.logger.info('CPE starting: {}'.format(str(ctx.instance.runtime_properties)))
