import argparse
import pickle

def hmdb51_parse_opts():
    """
    Data preprocess:
        Input: (0-255)
        Preprocess: 
            Temporal: 
            Spatial: Crop, Random Horizontally Flip, Norm.
            Temporal: Random Crop Frames.
    
    """
    parser = argparse.ArgumentParser()
    
    # parameters for loading data
    parser.add_argument(
        '--dataset',
        default='hmdb51',
        type=str,
        help='The type of dataset. (ucf101 | hmdb51)')
    parser.add_argument(
        '--root_path',
        default='/home/jingjing/zhipeng/adv-attack-video/data',
        type=str,
        help='Root directory path of data')
    parser.add_argument(
        '--video_path',
        default='/home/jingjing/zhipeng/adv-attack-video/data/hmdb51-jpg',
        type=str,
        help='Directory path of Videos')
    parser.add_argument(
        '--annotation_path',
        default='/home/jingjing/zhipeng/adv-attack-video/data/hmdb51-annotation/hmdb51_1.json',
        type=str,
        help='Annotation file path')
    # assign by outer parser
    parser.add_argument(
        '--data_type',
        default='flow',
        type=str,
        help='RGB or Optical flow, (rgb | flow)')
    
    # parameters for spatial transforms
    parser.add_argument(
        '--flow_channels',
        default=3,
        type=int,
        help='Random Seed.')
    
    parser.add_argument(
        '--manual_seed',
        default=1024,
        type=int,
        help='Random Seed.')
    parser.add_argument(
        '--norm_value',
        default=1,
        type=int,
        help='Original pixels/norm_value')
    parser.add_argument(
        '--initial_scale',
        default=1.0,
        type=float,
        help='Initial scale for multiscale cropping')
    parser.add_argument(
        '--n_scales',
        default=5,
        type=int,
        help='Number of scales for multiscale cropping')
    parser.add_argument(
        '--no_mean_norm',
        action='store_true',
        help='If true, inputs are not normalized by mean.')
    parser.set_defaults(no_mean_norm=False)
    parser.add_argument(
        '--std_norm',
        action='store_true',
        help='If true, inputs are normalized by standard deviation.')
    parser.set_defaults(std_norm=False)
    parser.add_argument(
        '--train_crop',
        default='corner',
        type=str,
        help=
        'Spatial cropping method in training. random is uniform. corner is selection from 4 corners and 1 center.  (random | corner | center)'
    )
    parser.add_argument(
        '--sample_size',
        default=112,
        type=int,
        help='Height and width of inputs')
    parser.add_argument(
        '--scale_step',
        default=0.84089641525,
        type=float,
        help='Scale step for multiscale cropping')
    
    # parameters for temporal transforms
    parser.add_argument(
        '--sample_duration',
        default=16,
        type=int,
        help='Temporal duration of inputs')
    
    parser.add_argument(
        '--scale_in_test',
        default=1.0,
        type=float,
        help='Spatial scale in test')
    parser.add_argument(
        '--crop_position_in_test',
        default='c',
        type=str,
        help='Cropping method (c | tl | tr | bl | br) in test')
    # parameters for target transforms
    
    args = parser.parse_args()

    return args    

def ucf101_parse_opts():
    """
    Data preprocess:
        Input: (0-255)
        Preprocess: 
            Temporal: 
            Spatial: Crop, Random Horizontally Flip, Norm.
            Temporal: Random Crop Frames.
    
    """
    parser = argparse.ArgumentParser()
    
    # parameters for loading data
    parser.add_argument(
        '--dataset',
        default='ucf101',
        type=str,
        help='The type of dataset. (ucf101 | hmdb51)')
    parser.add_argument(
        '--root_path',
        default='/home/jingjing/zhipeng/adv-attack-video/data',
        type=str,
        help='Root directory path of data')
    parser.add_argument(
        '--video_path',
        default='/home/jingjing/zhipeng/adv-attack-video/data/UCF101-jpg',
        type=str,
        help='Directory path of Videos')
    parser.add_argument(
        '--annotation_path',
        default='/home/jingjing/zhipeng/adv-attack-video/data/UCF101-annotation/ucfTrainTestlist/ucf101_01.json',
        type=str,
        help='Annotation file path')
    parser.add_argument(
        '--data_type',
        default='flow',
        type=str,
        help='RGB or Optical flow, (rgb | flow)')
    
    # parameters for spatial transforms
    parser.add_argument(
        '--flow_channels',
        default=3,
        type=int,
        help='Random Seed.')
    parser.add_argument(
        '--manual_seed',
        default=1024,
        type=int,
        help='Random Seed.')
    parser.add_argument(
        '--norm_value',
        default=1,
        type=int,
        help='Original pixels/norm_value')
    parser.add_argument(
        '--initial_scale',
        default=1.0,
        type=float,
        help='Initial scale for multiscale cropping')
    parser.add_argument(
        '--n_scales',
        default=5,
        type=int,
        help='Number of scales for multiscale cropping')
    parser.add_argument(
        '--no_mean_norm',
        action='store_true',
        help='If true, inputs are not normalized by mean.')
    parser.set_defaults(no_mean_norm=False)
    parser.add_argument(
        '--std_norm',
        action='store_true',
        help='If true, inputs are normalized by standard deviation.')
    parser.set_defaults(std_norm=False)
    parser.add_argument(
        '--train_crop',
        default='corner',
        type=str,
        help=
        'Spatial cropping method in training. random is uniform. corner is selection from 4 corners and 1 center.  (random | corner | center)'
    )
    parser.add_argument(
        '--sample_size',
        default=112,
        type=int,
        help='Height and width of inputs')
    parser.add_argument(
        '--scale_step',
        default=0.84089641525,
        type=float,
        help='Scale step for multiscale cropping')
    
    # parameters for temporal transforms
    parser.add_argument(
        '--sample_duration',
        default=16,
        type=int,
        help='Temporal duration of inputs')
    parser.add_argument(
        '--scale_in_test',
        default=1.0,
        type=float,
        help='Spatial scale in test')
    parser.add_argument(
        '--crop_position_in_test',
        default='c',
        type=str,
        help='Cropping method (c | tl | tr | bl | br) in test')
    # parameters for target transforms
    
    args = parser.parse_args()

    return args    

if __name__ == '__main__':
    args = hmdb51_parse_opts()
    dict_args = vars(args)
    with open('./hmdb51_params.pkl', 'wb') as opt:
        pickle.dump(dict_args, opt)
    
    args = ucf101_parse_opts()
    dict_args = vars(args)
    with open('./ucf101_params.pkl', 'wb') as opt:
        pickle.dump(dict_args, opt)
    