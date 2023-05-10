package com.KP.News.model;

import com.google.gson.annotations.SerializedName;

import java.io.Serializable;
import java.util.List;

public class NewsBO implements Serializable {
    public String status;
    public String totalResults;
    public List<ArticlesBO> articles;

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getTotalResults() {
        return totalResults;
    }

    public void setTotalResults(String totalResults) {
        this.totalResults = totalResults;
    }

    public List<ArticlesBO> getArticles() {
        return articles;
    }

    public void setArticles(List<ArticlesBO> articles) {
        this.articles = articles;
    }
}
