"""
Test the running status of Monit service
"""
import logging

import pytest

logger = logging.getLogger(__name__)

pytestmark = [
    pytest.mark.topology('any')
]


def test_monit_service_status(duthost):
    """
    @summary: Test the running status of Monit service by analyzing the command
              output of "sudo systemctl status monit.service | grep Active".
    """
    monit_service_status_info = duthost.shell("sudo systemctl status monit.service | grep Active")

    status_line = monit_service_status_info["stdout_lines"][0].strip()
    if "active" in status_line:
        logger.info("Monit service is running.")
    else:
        pytest.fail("Monit service is not running.")