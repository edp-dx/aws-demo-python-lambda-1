package com.mydomain;

import com.mydomain.service.HelloService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest
public class HelloServiceTest {

    @Autowired
    private HelloService helloService;

    @Test
    public void testGetHello() {
        assertThat(helloService.getHello().getMessage()).isEqualTo("Hello, World!");
    }
}
