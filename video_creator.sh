
#Create video
cd random_shape
python random_shaper.py;
cd ..
echo "Video Created"

duration=$(cat "combiner/video_length.txt")

#Extrapolate audio clip
cd music_taker
python take.py "$duration"
cd ..

#unisci audio e video
cd combiner
python combiner.py
cd ..

#upload del videoclip
mv combiner/result.mp4 video_uploader/video.mp4
cd video_uploader
python upload_video.py --file="video.mp4" \
                       --title="title goes here" \
                       --description="description goes here" \
                       --keywords="yup, keywords go here" \
                       --category="22" \
                       --privacyStatus="private"
                       #change privacy status tu public to make videos public
cd ../combiner
rm music.mp3
rm video.avi
rm video_length.txt
echo "Video Uploaded successfully and junk files eliminated"


