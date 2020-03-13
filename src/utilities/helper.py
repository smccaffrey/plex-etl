class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

class Movie:

    @staticmethod
    def move(new_dir, source_full, desination_full):
        return
        # old_full_path = os.path.join(transformed, movie)
        # dir_name = os.path.join(movie_lib_loc, movie.split('.')[0])
        # os.mkdir(dir_name)
        # new_full_path = os.path.join(dir_name, movie)
        # shutil.move(old_full_path, new_full_path)