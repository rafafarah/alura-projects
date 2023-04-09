package com.apiexample.api.languages;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "mainLanguages")
public class Language {

    @Id
    private String id;
    private String languageName;
    private String languageUrl;
    private int ranking;

    public Language() {

    }

    public Language(String languageName, String languageUrl, int ranking) {
        this.languageName = languageName;
        this.languageUrl = languageUrl;
        this.ranking = ranking;
    }

    public String getLanguageName() {
        return languageName;
    }
    public String getLanguageUrl() {
        return languageUrl;
    }
    public int getRanking() {
        return ranking;
    }
    public String getId() {
        return id;
    }
}
