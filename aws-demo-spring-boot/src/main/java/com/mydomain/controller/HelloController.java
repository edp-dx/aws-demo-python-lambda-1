package com.mydomain.controller;

import com.mydomain.model.Hello;
import com.mydomain.service.HelloService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/hello")
public class HelloController {

    @Autowired
    private HelloService helloService;

    @GetMapping
    public Hello getHello() {
        return helloService.getHello();
    }
}
