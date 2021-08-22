from omegaconf import OmegaConf


def read_url_confing():
    conf = OmegaConf.load('config/url_config.yaml')
    return conf
