{
 "cells": [
  {
   "cell_type": "raw",
   "id": "2f3f6893-00d3-4b2d-9ee8-bf6e10c5dd4a",
   "metadata": {},
   "source": [
    "Are there any artists who perform consistently pre-covid and post covid? \n",
    "From Data collected, list artists that performed consistently pre-covid and post-covid. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc407afb-79ab-41b8-8cc9-fe3e10f29b0a",
   "metadata": {},
   "source": [
    "Taylor Swift Post-Covid vs Pre Covid\n",
    "#Use Spotify artists API to collect albums released "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "cfbb48bf-5f37-444b-94fa-94a5c90966cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "7a87314c-e86c-433a-ab64-b5bfeed5ba5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1989 (Taylor's Version) [Deluxe]\n",
      "1989 (Taylor's Version)\n",
      "Speak Now (Taylor's Version)\n",
      "Midnights (The Til Dawn Edition)\n",
      "Midnights (3am Edition)\n",
      "Midnights\n",
      "Red (Taylor's Version)\n",
      "Fearless (Taylor's Version)\n",
      "evermore (deluxe version)\n",
      "evermore\n",
      "folklore: the long pond studio sessions (from the Disney+ special) [deluxe edition]\n",
      "folklore (deluxe version)\n",
      "folklore\n",
      "Lover\n",
      "reputation\n",
      "reputation Stadium Tour Surprise Song Playlist\n",
      "1989 (Deluxe)\n",
      "1989\n",
      "Red (Deluxe Edition)\n",
      "Speak Now World Tour Live\n",
      "Speak Now\n",
      "Speak Now (Deluxe Package)\n",
      "Fearless (Platinum Edition)\n",
      "Fearless (International Version)\n",
      "Live From Clear Channel Stripped 2008\n",
      "Taylor Swift\n"
     ]
    }
   ],
   "source": [
    "results = sp.artist_albums(taylor_uri, album_type='album')\n",
    "albums = results['items']\n",
    "while results['next']:\n",
    "    results = sp.next(results)\n",
    "    albums.extend(results['items'])\n",
    "\n",
    "for album in albums:\n",
    "    print(album['name'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ea00d20c-53b6-4f33-94cd-e8c047f5fe9c",
   "metadata": {},
   "source": [
    "Create a Dataframe comparing artists performance before Covid and after Covid. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "fa95071a-8d3f-471a-b075-094b7ed16013",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Artist</th>\n",
       "      <th>ALBUMS RELEASED before COVID-19</th>\n",
       "      <th>Performance before COVID-19</th>\n",
       "      <th>ALBUMS RELEASED Post-COVID-19</th>\n",
       "      <th>Performance after COVID-19</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Taylor Swift</td>\n",
       "      <td>6 albums</td>\n",
       "      <td>Very Popular</td>\n",
       "      <td>8 albums</td>\n",
       "      <td>Very Popular</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Artist ALBUMS RELEASED before COVID-19 Performance before COVID-19  \\\n",
       "0  Taylor Swift                        6 albums                Very Popular   \n",
       "\n",
       "  ALBUMS RELEASED Post-COVID-19 Performance after COVID-19  \n",
       "0                      8 albums               Very Popular  "
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Import Dependecies\n",
    "import pandas as pd\n",
    "# Create a DataFrame from a list of dictionaries.\n",
    "taylorswift_df = pd.DataFrame([\n",
    "    {\"Artist\": \"Taylor Swift\", \"ALBUMS RELEASED before COVID-19\": \"6 albums\", \n",
    "    \"Performance before COVID-19\": \"Very Popular\", \"ALBUMS RELEASED Post-COVID-19\": \"8 albums\", \"Performance after COVID-19\": \"Very Popular\"},\n",
    "])\n",
    "taylorswift_df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f40fd886-4786-4454-887e-b8612644772e",
   "metadata": {},
   "source": [
    "Drake Pre covid vs Post covid \n",
    "#Use Spotify artists API to collect albums released "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "cb75addd-6ca5-4f1a-a2e5-3337a06352bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "drake_uri = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "6a77dcd0-9a4c-47e3-ad15-7c5ab2d1a914",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "For All The Dogs Scary Hours Edition\n",
      "For All The Dogs\n",
      "Her Loss\n",
      "Honestly, Nevermind\n",
      "Certified Lover Boy\n",
      "Dark Lane Demo Tapes\n",
      "Care Package\n",
      "Scorpion\n",
      "More Life\n",
      "Views\n",
      "What A Time To Be Alive\n",
      "If You're Reading This It's Too Late\n",
      "Nothing Was The Same (Deluxe)\n",
      "Nothing Was The Same\n",
      "Take Care (Deluxe)\n",
      "Thank Me Later (Int'l Version)\n",
      "So Far Gone\n"
     ]
    }
   ],
   "source": [
    "results = sp.artist_albums(drake_uri, album_type='album')\n",
    "albums = results['items']\n",
    "while results['next']:\n",
    "    results = sp.next(results)\n",
    "    albums.extend(results['items'])\n",
    "\n",
    "for album in albums:\n",
    "    print(album['name'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "5ac3717c-f97c-4eb7-9877-a027de476d27",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Artist</th>\n",
       "      <th>ALBUMS RELEASED before COVID-19</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>ALBUMS RELEASED post COVID-19</th>\n",
       "      <th>Popularity post COVID-19</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Drake</td>\n",
       "      <td>10</td>\n",
       "      <td>Very Popular</td>\n",
       "      <td>7</td>\n",
       "      <td>Very Popular</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Artist  ALBUMS RELEASED before COVID-19    Popularity  \\\n",
       "0  Drake                               10  Very Popular   \n",
       "\n",
       "   ALBUMS RELEASED post COVID-19 Popularity post COVID-19  \n",
       "0                              7             Very Popular  "
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a DataFrame from a list of dictionaries.\n",
    "drake_df = pd.DataFrame([\n",
    "    {\"Artist\": \"Drake\", \"ALBUMS RELEASED before COVID-19\": 10,\n",
    "     \"Popularity\": \"Very Popular\", \"ALBUMS RELEASED post COVID-19\": 7, \"Popularity post COVID-19\": \"Very Popular\"},\n",
    "])\n",
    "drake_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c87a448-6be2-45e7-95d1-c61f0b32a090",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a74c647-ba8b-4e90-84ee-b3f92df4b644",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
