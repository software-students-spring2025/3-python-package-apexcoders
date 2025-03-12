import pytest,datetime
from game_master import spin_the_bottle, countdown


class Tests:

  def test_spin_the_bottle(self):
    name_list= ["Rin","Elena","Tony","Corrine"]
    actual = spin_the_bottle(name_list).split()[0]
    assert isinstance(actual, str), f"Expected spin_the_bottle() to return a string. Instead, it returned {actual}"
    assert len(actual) > 0, f"Expected spin_the_bottle() not to be empty. Instead, it returned a string with {len(actual)} characters"
    assert actual in name_list
  
  def test_countdown(self):
    t=3

    now = datetime.datetime.now()
    expected_low = now + datetime.timedelta(seconds=t)
    expected_high = now + datetime.timedelta(seconds=t+1)
    actual = countdown(t)

# start_time <= time_to_check <= end_time
    print(f"expected lowtime: {expected_low}")
    print(f"expected hightime: {expected_high}")
    print(f"Time after 10 seconds: {actual}")
    print(expected_low <= actual <= expected_high)

