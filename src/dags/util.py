import pendulum


def get_current_time_str() -> str:
    return pendulum.now().format("YYYY-MM-DD-HH:mm:ss")


def get_materialization_key(context) -> str:
    asset_name = context.asset_key.path[-1]
    return f"{asset_name}/{asset_name}_{get_current_time_str()}"
