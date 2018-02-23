#from redditdownload import print_progress_bar


def print_progress_bar(posts_downloaded, posts_requested):
    # Use TOTAL instead of DOWNLOADED when implementing, because we want to include the "already downloaded" files into
    # the progress bar for completion.

    progress_percent = float(posts_downloaded)/float(posts_requested) * 100
    progress_bar = ''
    progress_bar_width = 30
    for i in range(1, progress_bar_width + 1):
        if i <= (progress_percent / (10 / (progress_bar_width / 10))):
            progress_bar = '{}{}'.format(progress_bar, '=')
        else:
            progress_bar = '{}{}'.format(progress_bar, ' ')

    progress_bar_message = '{0}% [{1}] {2}/{3}'.format(progress_percent, progress_bar, posts_downloaded,
                                                       posts_requested)
    print(progress_bar_message)
    return


if __name__ == '__main__':
    #TOTAL = 1453
    TOTAL = 9053
    ARGSnum = 10000
    print_progress_bar(TOTAL, ARGSnum)
