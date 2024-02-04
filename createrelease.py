import fileinput

replaceTexts = {
    '#COVER_ART':'',
    '#TITLE':'ver2ion - ',
    '#ARTIST':'ver2ion',
    '#SONG_TITLE':'songtitle',
    '#RELEASE_DATE':'release',

    '#SOUNDCLOUD':'sc',
    '#SPOTIFY':'spt',
    '#APPLE_MUSIC':'aple',
    '#ITUNES':'itunes',
    '#YOUTUBE':'youtube',
    '#YOUTUBE_MUSIC':'youtubemusic',
    '#DEEZER':'dezer',
}
# replaceTexts = {
#     '#COVER_ART':'',
#     '#TITLE':'',
#     '#ARTIST':'',
#     '#SONG_TITLE':'',
#     '#RELEASE_DATE':'',

#     '#SOUNDCLOUD':'',
#     '#SPOTIFY':'',
#     '#APPLE_MUSIC':'',
#     '#ITUNES':'',
#     '#YOUTUBE':'',
#     '#YOUTUBE_MUSIC':'',
#     '#DEEZER':'',
# }
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