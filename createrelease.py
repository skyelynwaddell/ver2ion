import fileinput

replaceTexts = {
    '#COVER_ART':'',
    '#TITLE':'ver2ion - ',
    '#ARTIST':'ver2ion',
    '#SONG_TITLE':'songtitle',
    '#RELEASE_DATE':'releasedate',

    '#SOUNDCLOUD':'sc',
    '#SPOTIFY':'sptfy',
    '#ITUNES':'itunes',
    '#YOUTUBE':'youtube',
    '#YOUTUBE_MUSIC':'youtubemusic',
    '#DEEZER':'deezer',
}

for line in fileinput.input('template.html', inplace=True):
    for searchText in replaceTexts:
        replaceText = replaceTexts[searchText]
        line = line.replace(searchText,replaceText)
    print(line, end='')

for line in fileinput.input('template.css', inplace=True):
    for searchText in replaceTexts:
        replaceText = replaceTexts[searchText]
        line = line.replace(searchText,replaceText)
    print(line, end='')