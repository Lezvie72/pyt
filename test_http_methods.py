# -*- coding: utf-8 -*-

import allure
import pytest
import requests

from config.links import HttpMethods


@allure.feature('HTTP Methods')
@allure.story('Testing different HTTP verbs')
class TestHttpMethods:

    @allure.feature('can GET request')
    @pytest.mark.need_review
    def test_get(self):
        with allure.step("The request's query parameters."):
            r = requests.get(HttpMethods.GET)

        assert r.status_code == 200
        assert r.content

    @allure.feature('can DELETE request')
    @pytest.mark.need_review
    def test_delete(self):
        with allure.step("The request's DELETE parameters."):
            r = requests.delete(HttpMethods.DELETE)

        assert r.status_code == 200
        assert r.content

    @allure.feature('can PATCH request')
    @pytest.mark.need_review
    def test_patch(self):
        with allure.step("The request's PATCH parameters."):
            r = requests.patch(HttpMethods.PATCH)

        assert r.status_code == 200
        assert r.content

    @allure.feature('can POST request')
    @pytest.mark.need_review
    def test_post(self):
        with allure.step("The request's POST parameters."):
            r = requests.post(HttpMethods.POST)

        assert r.status_code == 200
        assert r.content

    @allure.feature('can PUT request')
    @pytest.mark.need_review
    def test_put(self):
        with allure.step("The request's PUT parameters."):
            r = requests.put(HttpMethods.PUT)

        assert r.status_code == 200
        assert r.content
