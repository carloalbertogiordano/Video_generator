
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
                       --title="#Shorts Randomically generated patterns!" \
                       --description="#Shorts #shortsclip #shortscraft #youtube #youtuber #subscribe #shortsadoptme \
                       #shortsroblox #shortsanity #shortsbeta #shortsfunny #shortsasmr #shortsart #shortscooking \
                       #shortscrochet #shortsbyamritamam #shortschallenge #shortscomplitition #shortsblackpink \
                      #instagramyoutube #youtuberlikes #youtubevide #shortscomedy #shortstiktok #shortsfortnite \
                      #shortsbts #shortsbhaiveersinghji #shortsbgmi #shortsassam #shortsads #youtubegrowth \
                      #youtubeusers #instavideo" \
                       --keywords="shapes random fun music" \
                       --category="22" \
                       --privacyStatus="public"
cd ../combiner
rm music.mp3
rm video.avi
rm video_length.txt
echo "Video Uploaded successfully and junk files eliminated"


