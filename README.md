# discoMoji

Repo for scraping emojis from discordmojis.com/slackmoji.com (They are the same site. 🤫)

# Dependancies

1. You will need to have python installed on your machine.

You can download it here:
https://www.python.org/downloads/

2. you will also need a [package](https://www.gnu.org/software/wget/) called `wget`.

You can install this with [Homebrew](https://brew.sh/) if you need to:
```sh
brew install wget
```


# Usage
To run the scraper yourself: (Linux and Mac only. (Sorry, Window people. 🫣🪟))

1. Open a terminal
2. Clone this repository
```sh
git clone https://git.mylegendary.quest/twizzay/discoMoji.git
```
3. Navigate to the cloned repository
```sh
cd discoMoji
```
4. Run the provided shell script
```sh
./run.sh
```
5. Watch the magic happen 🪄

---

This will first scrape for current emojis being listed on discordmoji.com. Then, it will download them to a directory adjacent to `discordMoji` called `scraped_emojis`

There are currently over 5000 emojis on this site as of this commit. A total of ~100M.

This script is written to be somewhat respectful of the host server. So, it will take a while for all of them to download (Over 1.5 hours.) Don't whine to me about it. It was the right thing to do.

Go outside for a little bit or something. 🌲🌳🌻
