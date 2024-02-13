import fileinput

replaceTexts = {
    '#COVER_ART':'https://s3.amazonaws.com/gather.fandalism.com/3000x3000%2D1197190%2D%2DD7A2CFEA%2D0A0B%2D4D2D%2D80581A9E82C13913%2D%2D0%2D%2D1696534%2D%2Dver2iongoodprod.9dmbeats.jpg',
    '#TITLE':'ver2ion - good',
    '#ARTIST':'ver2ion',
    '#SONG_TITLE':'good',
    '#RELEASE_DATE':'February 18 2024',

    '#SOUNDCLOUD':'',
    '#SPOTIFY':'',
    '#ITUNES':'',
    '#YOUTUBE':'',
    '#YOUTUBE_MUSIC':'',
    '#DEEZER':'',
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