# -*- coding: utf-8 -*-

import allure
import pytest
import requests

from config.links import StatusCodes


@allure.feature('Status codes')
@allure.story('Testing generates responses with given status code')
class TestStatusCodes:

    @allure.feature('can GET request')
    @pytest.mark.need_review
    @pytest.mark.parametrize('code', (no if no != 100 else pytest.param(no, marks=pytest.mark.xfail) for no in range(100, 501, 100)))
    def test_get(self, code):
        with allure.step("Return status code or random status code if more than one are given"):
            url = StatusCodes.STATUS + "/{}".format(code)

            try:
                r = requests.get(url, timeout=5)
            except requests.exceptions.Timeout as e:
                msg = "Error GET request {}".format(url)
                print(msg)
                pytest.fail(msg)

        assert r.status_code == code

    @allure.feature('can DELETE request')
    @pytest.mark.need_review
    @pytest.mark.parametrize('code', (no if no != 100 else pytest.param(no, marks=pytest.mark.xfail) for no in range(100, 501, 100)))
    def test_delete(self, code):
        with allure.step("Return status code or random status code if more than one are given"):
            url = StatusCodes.STATUS + "/{}".format(code)

            try:
                r = requests.delete(url, timeout=5)
            except requests.exceptions.Timeout as e:
                msg = "Error DELETE request {}".format(url)
                print(msg)
                pytest.fail(msg)

        assert r.status_code == code

    @allure.feature('can PATCH request')
    @pytest.mark.need_review
    @pytest.mark.parametrize('code', (no if no != 100 else pytest.param(no, marks=pytest.mark.xfail) for no in range(100, 501, 100)))
    def test_patch(self, code):
        with allure.step("Return status code or random status code if more than one are given"):
            url = StatusCodes.STATUS + "/{}".format(code)

            try:
                r = requests.patch(url, timeout=5)
            except requests.exceptions.Timeout as e:
                msg = "Error PATCH request {}".format(url)
                print(msg)
                pytest.fail(msg)

        assert r.status_code == code

    @allure.feature('can POST request')
    @pytest.mark.need_review
    @pytest.mark.parametrize('code', (no if no != 100 else pytest.param(no, marks=pytest.mark.xfail) for no in range(100, 501, 100)))
    def test_post(self, code):
        with allure.step("Return status code or random status code if more than one are given"):
            url = StatusCodes.STATUS + "/{}".format(code)

            try:
                r = requests.post(url, timeout=5)
            except requests.exceptions.Timeout as e:
                msg = "Error POST request {}".format(url)
                print(msg)
                pytest.fail(msg)

        assert r.status_code == code

    @allure.feature('can PUT request')
    @pytest.mark.need_review
    @pytest.mark.parametrize('code', (no if no != 100 else pytest.param(no, marks=pytest.mark.xfail) for no in range(100, 501, 100)))
    def test_put(self, code):
        with allure.step("Return status code or random status code if more than one are given"):
            url = StatusCodes.STATUS + "/{}".format(code)

            try:
                r = requests.put(url, timeout=5)
            except requests.exceptions.Timeout as e:
                msg = "Error PUT request {}".format(url)
                print(msg)
                pytest.fail(msg)

        assert r.status_code == code
