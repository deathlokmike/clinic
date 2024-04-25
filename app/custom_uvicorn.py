from uvicorn.workers import UvicornWorker


class CustomUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {"loop": "asyncio",
                     "log_level": "info",
                     "http": "auto",
                     "proxy_headers": True,
                     "forwarded_allow_ips": "*"
                     }
