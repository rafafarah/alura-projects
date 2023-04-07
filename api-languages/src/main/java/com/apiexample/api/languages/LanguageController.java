package com.apiexample.api.languages;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LanguageController {

    @Autowired
    private LanguageRepository repository;

    @GetMapping(value = "/favorite-language")
    public String getFavoriteLanguage() {
        return "Hi, Jawa!";
    }

    @GetMapping("/languages")
    public List<Language> getLanguageList() {
        return repository.findAll();
    }
}
