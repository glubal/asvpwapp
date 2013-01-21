import math

ring_colours = ('transparent',
                'white',
                'white',
                'black',
                'black',
                'blue',
                'blue',
                'red',
                'red',
                'yellow',
                'yellow')

def index():
    # Show main page to enter a user's score
    html = dict()
    
    # The target is always square, so target_size = width = height
    # TODO: Calculate this based on the browser's size
    target_size = 100
    
    target_grid = []
    for y in range(0, target_size):
        target_grid[y] = []
        for x in range(0, target_size):
            dist = __distance_to_centre(x, y, target_size)
            hit_value = int((dist / target_size) * 10)
            pixel_file_name = '%s_pixel.png' % ring_colours[hit_value]
            A(IMG(_src=URL('static',pixel_file_name), _alt="."), _href=URL('score','add', args=hit_value))
    
    html['big_target'] = TABLE(target_grid)
    return html


def __distance_to_centre(x, y, target_size):
    target_diameter = target_size / 2
    return math.sqrt((abs(target_diameter - x)**2) +
                     (abs(target_diameter - y)**2))


def add():
    # Add a result to the user's score
    pass


def confirm():
    # Confirm the entered round score
    pass