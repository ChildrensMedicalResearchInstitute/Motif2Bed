import logging
import os
import errno


def file_exists(data_file, must_exist=False):
    '''
    |
    | Function that test if a file exists
    |
    |
    |  Parameters
    |  ----------
    |  data_file : Path to the file
    |  must_exist : A boolean (default False), if True the code will stop
    |
    |  Returns
    |  -------
    |  boolean: True if the file exists
    |
    '''
    is_dir =False
    if os.path.exists(data_file):
        if not os.path.isdir(data_file):
            return True
        is_dir =True

    if must_exist:
        if is_dir:
            logging.error('%s is a directory!', data_file)
        else:
            logging.error('File %s does not exist!', data_file)
        exit(errno.ENOENT)
    else :
        return False


def get_cmri_logger():
    log_formatter = logging.Formatter('CMRI Bioinformatics %(levelname)s [%(asctime)s] | %(message)s')
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    return root_logger, log_formatter


epilog_text = "Children's Medical Research Institute - Bioinformatics team "

def print_cmri_welcome( name):
    logging.info( "-----------------------------------------------")
    logging.info( "   ______     __    __     ______     __       ")
    logging.info( '  /\  ___\   /\ "-./  \   /\  == \   /\ \      ')
    logging.info( "  \ \ \____  \ \ \-./\ \  \ \  __<   \ \ \     ")
    logging.info( "   \ \_____\  \ \_\ \ \_\  \ \_\ \_\  \ \_\    ")
    logging.info( "    \/_____/   \/_/  \/_/   \/_/ /_/   \/_/    ")
    logging.info( "")
    logging.info( "---- Children’s Medical Research Institute ----")
    logging.info( " Finding cures for childhood genetic diseases  ")
    logging.info( "")
    logging.info( " ==============================================")
    logging.info( " "+name)
    logging.info( " Author: Pablo Galaviz             ")
    logging.info( " pgalaviz@cmri.org.au              ")
    logging.info( " ==============================================")
    logging.info( "")

