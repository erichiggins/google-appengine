#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Errors used in the urlfetch API
developers.
"""






class Error(Exception):
  """Base URL fetcher error type."""


class InvalidURLError(Error):
  """Raised when the URL given is empty or invalid.

  Only http: and https: URLs are allowed. The maximum URL length
  allowed is 2048 characters. The login/pass portion is not
  allowed. In deployed applications, only ports 80 and 443 for http
  and https respectively are allowed.
  """


class DownloadError(Error):
  """Raised when the we could not fetch the URL for any reason.

  Note that this exception is only raised when we could not contact the
  server. HTTP errors (e.g., 404) are returned in as the status_code field
  in the return value of Fetch, and no exception is raised.
  """


class ResponseTooLargeError(Error):
  """Raised when the response was too large and was truncated."""
  def __init__(self, response):
    self.response = response


class InvalidMethodError(Error):
  """Raised when an invalid value for 'method' is provided"""


class InvalidMethodError(Error):
  """Raised when an invalid value for 'method' is provided"""
