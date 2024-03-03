import fileinput

replaceTexts = {
    '#COVER_ART':'https://s3.amazonaws.com/gather.fandalism.com/1197190%2D%2D42B14099%2DB251%2D4CB5%2DA5F4EA7105CDF345%2D%2D0%2D%2D1862864%2D%2Dver2ioncantholdmebackprod.ymvu.wav.png',
    '#TITLE':'ver2ion - hazy pack',
    '#ARTIST':'ver2ion',
    '#SONG_TITLE':'hazy pack',
    '#RELEASE_DATE':'March 3 2024',

    '#SOUNDCLOUD':'https://soundcloud.com/ver2ion/ver2ion-hazy-pack-prod-ymvuwav-1',
    '#SPOTIFY':'',
    '#ITUNES':'',
    '#YOUTUBE':'https://www.youtube.com/watch?v=xQjVEMtVpWk',
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