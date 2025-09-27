import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="para8 1_logs.log",
                    filemode="w",
                    format="We have a message:%(asctime)s:@:%(levelname)s - %(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

logging.debug("debug2")
logging.info("info2")