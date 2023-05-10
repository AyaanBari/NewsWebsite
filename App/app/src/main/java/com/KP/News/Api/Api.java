package com.KP.News.Api;

import com.KP.News.model.NewsBO;

import retrofit2.Call;
import retrofit2.http.GET;

public interface Api {
    String BASE_URL = "https://newsapi.org/v2/";

    @GET("top-headlines?country=in&apiKey=fbf5d7635e8b4bc981b1e6a4881d4865")
    Call<NewsBO> getsuperHeroes();

    @GET("top-headlines?country=in&category=sports&apiKey=fbf5d7635e8b4bc981b1e6a4881d4865")
    Call<NewsBO> getsuperSports();

    @GET("top-headlines?country=in&category=politics&apiKey=fbf5d7635e8b4bc981b1e6a4881d4865")
    Call<NewsBO> getsuperpolitics();

    @GET("top-headlines?country=in&category=technology&apiKey=fbf5d7635e8b4bc981b1e6a4881d4865")
    Call<NewsBO> getsupertechnlogy();

    @GET("top-headlines?country=in&category=entertainment&apiKey=fbf5d7635e8b4bc981b1e6a4881d4865")
    Call<NewsBO> getsuperentertainment();

}
//https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=fbf5d7635e8b4bc981b1e6a4881d4865