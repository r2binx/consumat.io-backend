from consumatio.gateways.movie_details_to_dict import *


def test_movie_details_to_dict():
    json = {
        "adult":
        False,
        "backdrop_path":
        "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
        "belongs_to_collection":
        None,
        "budget":
        63000000,
        "genres": [{
            "id": 18,
            "name": "Drama"
        }],
        "homepage":
        "",
        "id":
        550,
        "imdb_id":
        "tt0137523",
        "original_language":
        "en",
        "original_title":
        "Fight Club",
        "overview":
        "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
        "popularity":
        0.5,
        "poster_path":
        None,
        "production_companies": [{
            "id": 508,
            "logo_path": "/7PzJdsLGlR7oW4J0J5Xcd0pHGRg.png",
            "name": "Regency Enterprises",
            "origin_country": "US"
        }],
        "production_countries": [{
            "iso_3166_1": "US",
            "name": "United States of America"
        }],
        "release_date":
        "1999-10-12",
        "revenue":
        100853753,
        "runtime":
        139,
        "spoken_languages": [{
            "iso_639_1": "en",
            "name": "English"
        }],
        "status":
        "Released",
        "tagline":
        "How much can you know about yourself if you've never been in a fight?",
        "title":
        "Fight Club",
        "video":
        False,
        "vote_average":
        7.8,
        "vote_count":
        3439
    }

    dict = {
        "code": 550,
        "title": "Fight Club",
        "genres": [{
            "name": "Drama"
        }],
        "overview":
        "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
        "popularity": 0.5,
        "vote_average": 7.8,
        "release_date": "1999-10-12",
        "runtime": 139,
        "status": "Released"
    }

    assert movie_details_to_dict(json) == dict