# Music-Service-API

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!--
[![Build Status](https://travis-ci.com/travis-ci/travis-web.svg?branch=main)](https://travis-ci.com/github/2008-Untangled/Music-Service-API)
-->

  <h3 align="center">Music Service API</h3>

  <p align="center">
    This is a microservice that was built to provide music information to the Untangled application.  When receiving a request for a song, this microservice consumes the <a href="https://developer.spotify.com/documentation/web-api/">Spotify API</a>, complies the relevant information, and returns that information in the response.
    <br />
    <a href="https://github.com/2008-Untangled"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- for adding a demo video
    <a href="Add our video link here">View Demo</a>  · -->
    ·
    <a href="https://github.com/2008-Untangled/Music-Service-API/issues">Report Bug</a>
    ·
    <a href="https://github.com/2008-Untangled/Music-Service-API/issues">Request Feature</a>
  </p>
</p>

### Table of Contents

1. [About This Project](#about-this-project)
1. [Virtual Environment setup](#virtual-environment-setup)
1. [Endpoint](#endpoint)
1. [Testing](#testing)
1. [Contributing](#contributing)
1. [Contact](#contact)

## About This Project
Visit [Untangled](https://github.com/2008-Untangled) to view all the repositories associated with this application.

This microservice allows you to query a song name and receive a response that includes the song name, artist name, album name, album release date, and a url for that song on spotify.  It takes in the song name query, then consumes the [Spotify API](https://developer.spotify.com/documentation/web-api/) to get information about that song.  The relevant information for that song is then extracted and compiled, and then returned in the microservice response.   

## Virtual Environment setup

```bash
# build a virtual environment to install your Python packages
python3 -m venv ./venv

# 'activate' the virtual environment for your project
# do this every time you start a new terminal and enter your project folder
source venv/bin/activate

# install your Python packages
pip3 install -r requirements.txt

#set your Spotify API keys
export SPOTIFY_CLIENT_ID=<your client id here>
export SPOTIFY_CLIENT_SECRET=<your client secret here>
```

To shut off your virtual environment, run `deactivate` at a terminal where you
have an active virtual environment.

## Endpoint

### Search for a track:  `http://127.0.0.1:5000/api/v1/track?<track_name_here>`

#### Example Valid Query:
```
GET http://127.0.0.1:5000/api/v1/track?yesterday
```
Response:
```
{
  "data": {
    "album_name": "Help! (Remastered)",
    "album_release_date": "1965-08-06",
    "artist_name": "The Beatles",
    "song": "Yesterday - Remastered 2009",
    "url": "https://open.spotify.com/track/3BQHpFgAp4l80e1XslIjNI"
  }
}
```

#### Example Empty Query:
```
GET http://127.0.0.1:5000/api/v1/track?
```
Response:
```
{
  "error": 422,
  "message": "Unprocessable Entity, please try another song title"
}
```

#### Example Invalid Query:
```
GET http://127.0.0.1:5000/api/v1/track?asdfgasdfgasd
```
Response:
```
{
  "message": "Unprocessable Entity, please try another song title",
  "status": 422
}
```


## Testing

To run tests first activate your virtual environment with `source venv/bin/activate`<br>
Then run `python3 -m pytest`


See [Open Issues](https://github.com/2008-Untangled/Music-Service-API/issues) or visit our [Project Board](https://github.com/orgs/2008-Untangled/projects/1) for a list of proposed features, known issues, and project extensions.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make this community such an amazing and fun place to learn, grow, and create! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch ```git checkout -b feature/NewGreatFeature```
3. Commit your Changes ```git commit -m 'Add some NewGreatFeature'```
4. Push to the Branch ```git push origin feature/NewGreatFeature```
5. Open a new Pull Request!


<!-- CONTACT -->
## Contact

Bryce Jarrett &nbsp;&nbsp;&nbsp;&nbsp; - [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/bryce-jarrett/) - [GitHub](https://github.com/brycemara)

Cameron Romo &nbsp; - [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/cameron-romo-64b3a69b/) - [GitHub](https://github.com/cameronRomo)

Joe Lopez &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/joseph-lopez-100/) - [GitHub](https://github.com/Codo-Baggins)

Estelle Staffieri &nbsp; - [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/estellestaffieri/) - [GitHub](https://github.com/Estaffieri)

Grant Dempsey &nbsp;- [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/grant-dempsey-8a9a16169/) - [GitHub](https://github.com/GDemps)

Eduardo Parra &nbsp;&nbsp;&nbsp; - [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/eduardo--parra/) - [GitHub](https://github.com/helloeduardo)

Jesse Mellinger &nbsp;&nbsp;- [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/jesse-mellinger/) - [GitHub](https://github.com/JesseMellinger)

Sean Steel &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/sean-steel/) - [GitHub](https://github.com/s-steel)



Project Link: [Untangled](https://github.com/2008-Untangled)



<!-- ACKNOWLEDGEMENTS -->
<!-- Add resources that were used to help create this project here -->




<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/2008-Untangled/Music-Service-API
[contributors-url]: https://github.com/2008-Untangled/Music-Service-API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/2008-Untangled/Music-Service-API
[forks-url]: https://github.com/2008-Untangled/Music-Service-API/network/members
[stars-shield]: https://img.shields.io/github/stars/2008-Untangled/Music-Service-API
[stars-url]: https://github.com/2008-Untangled/Music-Service-API/stargazers
[issues-shield]: https://img.shields.io/github/issues/2008-Untangled/Music-Service-API
[issues-url]: https://github.com/2008-Untangled/Music-Service-API/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
