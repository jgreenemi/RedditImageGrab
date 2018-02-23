#from redditdownload import print_progress_bar


def print_progress_bar(posts_downloaded, posts_requested):
    progress_percent = float(posts_downloaded)/float(posts_requested) * 100
    progress_bar = ''
    progress_bar_width = 30
    for i in range(1, progress_bar_width + 1):
        if i <= (progress_percent / (10 / (progress_bar_width / 10))):
            progress_bar = '{}{}'.format(progress_bar, '=')
        else:
            progress_bar = '{}{}'.format(progress_bar, ' ')

    progress_bar_message = '{0}% [{1}]'.format(progress_percent, progress_bar)
    print(progress_bar_message)
    return


if __name__ == '__main__':
    #DOWNLOADED = 1453
    DOWNLOADED = 9053
    ARGSnum = 10000
    print_progress_bar(DOWNLOADED, ARGSnum)
