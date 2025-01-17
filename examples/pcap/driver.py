import random
import netshare.ray as ray
from netshare import Generator

if __name__ == '__main__':
    # Change to False if you would not like to use Ray
    ray.config.enabled = False
    ray.init(address="auto")

    # configuration file
    generator = Generator(config="config_example_pcap_nodp.json")

    # `work_folder` should not exist o/w an overwrite error will be thrown.
    # Please set the `worker_folder` as *absolute path*
    # if you are using Ray with multi-machine setup
    # since Ray has bugs when dealing with relative paths.
    generator.train(work_folder='/data0/mxy/linchungang/NetShare/results/test-caida')
    generator.generate(work_folder='/data0/mxy/linchungang/NetShare/results/test-caida')
    generator.visualize(work_folder='/data0/mxy/linchungang/NetShare/results/test-caida')

    ray.shutdown()
