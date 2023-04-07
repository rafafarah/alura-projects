package com.apiexample.api.languages;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LanguageController {

    private List<Language> languageList =
        List.of(
            new Language("Java",
                "https://raw.githubusercontent.com/abrahamcalf/programming-languages-logos/master/src/java/java_256x256.png",
                2),
            new Language("C",
                "https://raw.githubusercontent.com/abrahamcalf/programming-languages-logos/master/src/c/c_256x256.png",
                1)
        );

    @GetMapping(value = "/favorite-language")
    public String getFavoriteLanguage() {
        return "Hi, Jawa!";
    }

    @GetMapping("/languages")
    public List<Language> getLanguageList() {
        return languageList;
    }
}
