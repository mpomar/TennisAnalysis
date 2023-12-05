<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO & HEADER -->
<br />
<div align="center">
  <a href="https://github.com/mpomar/TennisAnalysis">
    <img src="https://cdn-icons-png.flaticon.com/256/2387/2387401.png" alt="Logo" width="80">
  </a>

  <h3 align="center">Tennis Analysis</h3>

  <p align="center">
    A tool to help you in the comparative analysis of two tennis players!
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#understanding-the-data">Understanding The Data</a></li>
      </ul>
    </li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- BODY -->
## About The Project

This tool, developed for tennis enthusiasts and sports bettors, provides a swift comparative analysis of two tennis players based on essential metrics. Developed from personal insights into factors influencing match outcomes in Singles, it is ideal for users familiar with the intricacies of tennis data. Aimed at facilitating efficient decision-making, especially in sports betting scenarios, users are encouraged to acquaint themselves with the primary metrics before utilization.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Understanding The Data

It would take me ages to explain the theory behind this, but to summarize, these are the metrics I primarily consider:

* **Match percentage**: Serves as a key indicator of a player's current form. It offers a comprehensive view of the number of matches played and won by the players in the current year, considering all surfaces.
* **RPW/SPW ratio**: Analyzes the cross-section of service and return stats to gauge a player's defensive capabilities and advantages over their opponent. Example: A player excelling in receiving against an opponent with weak service indicates a significant advantage.
* **Raw Elo**: Leverages Tennis Abstract's Elo ratings, deemed more reliable than official ATP rankings. I tend to focus on the Raw Elo specific to the surface of the match under consideration.
* **Peak Match**: Identifies the pinnacle of a player's career based on Elo performance. Another indicator of a player's form: the more recent the peak match, the better. However, there are cases when this is irrelevant; learning when to take this into account requires time.
* **Wildcard / Qualifiers**: Draws attention to the impact of wildcards and qualifiers as potential surprises, particularly in the early stages of a tournament. There are psychological and motivational factors contributing to their unpredictability, hence I recommend considering this in the analysis as well.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Prerequisites

* Install all dependencies, included [Chromedriver](https://googlechromelabs.github.io/chrome-for-testing)
* Provide the path to Chromedriver in scraper.py 
* Once a year you might also want to update line 43 of scraper.py to ensure you take stats of the current year

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

* Run the script from main.py.
* Enter all the requested information.
* Wait for the script to generate the results.
* Review the results and make your own decision (again, it would take me a while to explain how I interpret the returned information).

Please note that for player names, they must match the format on Tennis Abstract.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request 

You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

M. Pomar - [@deliverymgt](https://twitter.com/deliverymgt.com) - m.pomar@outlook.com

Project Link: [https://github.com/mpomar/TennisAnalysis](https://github.com/mpomar/TennisAnalysis)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

First and foremost, I would like to express my gratitude to Tennis Abstract. 
This small project would not have been possible without the extensive data they have collected over the years and generously shared with the public on the Internet. 
It is undoubtedly the best resource available for tennis enthusiasts, and I strongly encourage you to delve deeper into their statistics for additional insights. 
While the script utilizes what, based on my experience, are the most crucial factors in evaluating a tennis match, there is much more valuable information to discover on their website. 
Keep up the excellent work, guys! ❤️

Other resources:

* [Shields.io](https://shields.io)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[forks-shield]: https://img.shields.io/github/forks/mpomar/TennisAnalysis?style=for-the-badge
[forks-url]: https://github.com/mpomar/TennisAnalysis/network/members
[stars-shield]: https://img.shields.io/github/stars/mpomar/TennisAnalysis?style=for-the-badge
[stars-url]: https://github.com/mpomar/TennisAnalysis/stargazers
[issues-shield]: https://img.shields.io/github/issues/mpomar/TennisAnalysis?style=for-the-badge
[issues-url]: https://github.com/mpomar/TennisAnalysis/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/manfredipomar
