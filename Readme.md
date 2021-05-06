# FlagPlanter

Sometimes you may have an idea, a sudden insight, that you want to stake a claim to, but you may not feel ready to reveal that idea to people just yet. The flag planter app can help us in that situation. 

## Simple but less secure method

If you have a text, or an image, or a video of less than 2GB size on your phone, then you can use this app to generate a unique hash of that digital asset. Then just copy-paste the hash and publish it on Twitter.  This way, in future you can claim that, you had access to either the content at the time the tweet was published, or atleast the hash itself. This is less secure, because once you publish the hash, somebody else can copy that bare-hash and 

## [In Progress] Negligibly more complex, but much more secure method

If you have a text, or an image, or a video of less than 2GB size on your phone then the app uses a custom salt, based on your unique email address, or username, or twitter handle to generate the hash of the digital asset. This way the person who really possesses the content will be able to make a truly personalized hash which cant be "stolen" by others. We merely have to look at the hash to see who created it.

## Technology

The app is written in python using Kivy. 

