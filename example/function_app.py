import func_az as fz

def make():
  import azure.functions as func
  from dslog import Logger
  logger = Logger.stdlib().prefix('[DFY JOBS]')
  idx = 0

  app = func.FunctionApp()

  @fz.job(app, 'pairings', route='pairings', timer='0 */5 * * * *')
  async def pairings():
    nonlocal idx
    logger('Updating pairings...')
    if idx % 2 == 1:
      raise ValueError('Oops some bad happened!')
    idx += 1

  return app


app = fz.startup(make)
  