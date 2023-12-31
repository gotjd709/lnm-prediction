K               = 50
PATH_TABLE_PATH = '/workspace/data/feature_extraction/path_table.csv'
SAVE_CSV_PATH   = '/workspace/data/feature_extraction/'
PROPERTIES      = [
        # tumor ratio
        'tot_tumor1_ratio', 
        'tot_tumor2_ratio', 
        'main_tumor1_ratio', 
        'main_tumor2_ratio',

        # total region all tumor
        'tot_all_num_region',
        'tot_all_area',
        'tot_all_convex_area',
        'tot_all_filled_area',
        'tot_all_perimeter',
        'tot_all_equiv_diameter',
        'tot_all_euler_number',
        'tot_all_mj_axis_length',
        'tot_all_mi_axis_length',
        # total region tumor1
        'tot_tumor1_num_region',
        'tot_tumor1_area',
        'tot_tumor1_convex_area',
        'tot_tumor1_filled_area',
        'tot_tumor1_perimeter',
        'tot_tumor1_equiv_diameter',
        'tot_tumor1_euler_number',
        'tot_tumor1_mj_axis_length',
        'tot_tumor1_mi_axis_length',
        # total region tumor2
        'tot_tumor2_num_region',
        'tot_tumor2_area' ,
        'tot_tumor2_convex_area',
        'tot_tumor2_filled_area',
        'tot_tumor2_perimeter' ,
        'tot_tumor2_equiv_diameter',
        'tot_tumor2_euler_number',
        'tot_tumor2_mj_axis_length',
        'tot_tumor2_mi_axis_length',

        # main region all tumor
        'main_all_area',
        'main_all_convex_area', 
        'main_all_filled_area',
        'main_all_perimeter',
        'main_all_equiv_diameter',
        'main_all_euler_number',
        'main_all_mj_axis_length',
        'main_all_mi_axis_length',
        'main_all_eccentricity',
        'main_all_extent',
        'main_all_solidity',
        'main_all_pa_ratio',
        'main_all_fractal_dimension',
        # main region tumor1
        'main_tumor1_area',
        'main_tumor1_convex_area', 
        'main_tumor1_filled_area',
        'main_tumor1_perimeter',
        'main_tumor1_equiv_diameter', 
        'main_tumor1_euler_number',
        'main_tumor1_mj_axis_length', 
        'main_tumor1_mi_axis_length', 
        'main_tumor1_all_eccentricity', 
        'main_tumor1_all_extent',
        'main_tumor1_all_solidity', 
        'main_tumor1_all_pa_ratio',
        'main_tumor1_all_fractal_dimension', 
        # main region tumor2
        'main_tumor2_area', 
        'main_tumor2_convex_area',
        'main_tumor2_filled_area',
        'main_tumor2_perimeter',
        'main_tumor2_equiv_diameter', 
        'main_tumor2_euler_number', 
        'main_tumor2_mj_axis_length',
        'main_tumor2_mi_axis_length',
        'main_tumor2_eccentricity', 
        'main_tumor2_extent',
        'main_tumor2_solidity',
        'main_tumor2_pa_ratio',
        'main_tumor2_fractal_dimension' 
    ]