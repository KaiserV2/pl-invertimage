#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
from importlib.metadata import Distribution

from chris_plugin import chris_plugin, PathMapper
from PIL import Image, ImageOps

__pkg = Distribution.from_name("invertimage")
__version__ = __pkg.version


DISPLAY_TITLE = r"""
       _        _                     _   _                            
      | |      (_)                   | | (_)                           
 _ __ | |______ _ _ ____   _____ _ __| |_ _ _ __ ___   __ _  __ _  ___ 
| '_ \| |______| | '_ \ \ / / _ \ '__| __| | '_ ` _ \ / _` |/ _` |/ _ \
| |_) | |      | | | | \ V /  __/ |  | |_| | | | | | | (_| | (_| |  __/
| .__/|_|      |_|_| |_|\_/ \___|_|   \__|_|_| |_| |_|\__,_|\__, |\___|
| |                                                          __/ |     
|_|                                                         |___/      
"""


parser = ArgumentParser(description='A ChRIS plugin to invert images',
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='foo',
                    help='argument which sets example output file name')
parser.add_argument('-V', '--version', action='version',
                    version=f'%(prog)s {__version__}')
parser.add_argument(
                        '--invert',
                        default     = '**/*jpg',
                        help        = '''Glob pattern to match all images to invert.'''
)

def invert_image(inputfile, outputfile):
    # if inputfile ends with jpg
    if str(inputfile).endswith(".jpg"):
        im = Image.open(inputfile)
    elif str(inputfile).endswith(".png"):
        im = Image.open(inputfile).convert('RGB')
    else:
        print("Please input with a jpg or png file")
    im_invert = ImageOps.invert(im)
    im_invert.save(outputfile)

# documentation: https://fnndsc.github.io/chris_plugin/chris_plugin.html#chris_plugin
@chris_plugin(
    parser=parser,
    title='Invert Image',
    category='',                 # ref. https://chrisstore.co/plugins
    min_memory_limit='2Gi',    # supported units: Mi, Gi
    min_cpu_limit='1000m',       # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0              # set min_gpu_limit=1 to enable GPU
)
def main(options: Namespace, inputdir: Path, outputdir: Path):
    """
    :param options: non-positional arguments parsed by the parser given to @chris_plugin
    :param inputdir: directory containing input files (read-only)
    :param outputdir: directory where to write output files
    """

    print(DISPLAY_TITLE)

    mapper = PathMapper.file_mapper(inputdir, outputdir,glob=options.invert)
    for input, output in mapper:
        # ld_result.append(segmentation_process(options, input, output))
        invert_image(input, output)
        print(f'Successfully inverted: {input} and stored it in: {output}')
        



if __name__ == '__main__':
    main()
