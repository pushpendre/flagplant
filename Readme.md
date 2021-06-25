# FlagPlanter

The OpenSource FlagPlanter application ([download apk](https://github.com/pushpendre/flagplant/blob/master/bin/ )) can be used for:

1. Protection against "Fake DeepFakes".
2. Proving possession of a digital artefact before a certain time.
3. Making prediction about the future without revealing the prediction.

 
# Demonstration

This video https://youtu.be/dZQBr1dxyNo demonstrates how the app works.

[![video](https://img.youtube.com/vi/dZQBr1dxyNo/0.jpg)](https://www.youtube.com/watch?v=dZQBr1dxyNo)



# Motivation: What is the problem that this app is solving?

Advancements in Deep Learning have made it possible for lay-persons to create photo-realistic computer generated images (CGI) cheaply. Such CGIs are called "DeepFakes". DeepFakes can be used to spread malicious lies and a lot of attention has been posed to the direct risk posed by deepfakes. However, deepfakes create an even bigger, indirect problem, that malicious actors can discredit genuinely real images by claiming that they are deepfakes. Similar concerns were raised in a recent report about an alleged deepfake of a teenager [link](https://www.dailydot.com/debug/deepfake-vaping-video-cheerleaders/). This potential for abuse is readily apparent to even a casual observer, as evident from the youtube screenshot below. So, my motivation is to prove that a real image is not a fake.  

<img src="https://i.imgur.com/Wmc4QMl.png" alt="ytcomment" width="500"/>

 A slightly different, secondary, problem that this app solves is of staking a claim to a content without revealing the content to the world. This is a niche problem that is important enough that developers have built [complicated web-services](https://futuu.re/) to support this use-case. This [ycombinator thread](https://news.ycombinator.com/item?id=26433589) also describes some other approaches.  My approach has the benefit that it does not require a web-service, just a simple UI that never needs to communicate to the web. Therefore, it is more secure. Moreover, my approach creates a human-readable and verifiable proof of content possession.

# Method

As I mention above, my motivation is to prove that a real image is not fake. However I actually solve a closely related problem of proving that a user possessed the given file before a certain time. Let's say that user possesses a digital artefact/content with value X at time t. The method comprises of the following steps:

1. The user selects a unique username. E.g. their email address. The app uses this user-specific string `U` as the `salt` in the `sha` encryption process.
2. The user generates a hash `H` of the content `X` using the salt `U`. The user-specific salt is appended to the hash. 
3. The user releases the concatenated salt and hash to the world at time `T`, through a channel that only they can write to. This can be a social media profile like twitter, or a blockchain. A blockchain has the benefit that the hash cannot be deleted once released, but it has the drawback that it's not tied to a person in a human-readable manner. 
 
In future, when content `X` is released to the public, then the public can check: 

- content `X`, when hashed using salt `U` results in hash `H` and it was released on user's profile at time `T`.  

This lets the public verify, in a human-readable fashion, that it was user `U` who created the hash. Since the hash was released on the user's profile at time `T`, therefore they must have possessed the content before time `T`, and no-body else could be impersonating them.

**How does this method prove the genuine-ness of a file?**

This method proves that the file existed before time `T` because otherwise we couldn't have released the hash. Releasing a hash may be much easier to do either due to bandwidth or due to privacy concerns, therefore releasing a hash is easier than releasing the full video.

**Related Work**

This method is a specific instance of a more general idea known as a [Commitment Scheme](https://en.wikipedia.org/wiki/Commitment_scheme). The main contribution of this work is that it provides a more easy-to-use and easy-to-understand UI on top of a commitment scheme. Moreover, I provide a way to use human-readable salts which makes the process of falsifying the origin of a hash very easy.

# Source Code and Binary

The app is written in python using Kivy. You can download a compiled apk at https://github.com/pushpendre/flagplant/blob/master/bin/ 

