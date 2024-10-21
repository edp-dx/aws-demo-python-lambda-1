package com.mydomain.service;

import com.mydomain.model.Hello;
import org.springframework.stereotype.Service;

@Service
public class HelloService {

    public Hello getHello() {
        Hello hello = new Hello();
        hello.setMessage("Hello, World!");
        return hello;
    }
}
