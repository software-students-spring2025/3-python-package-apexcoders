import pytest,datetime, random
from game_master import spin_the_bottle, countdown, random_multiple_people_punishment


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

    assert(expected_low <= actual <= expected_high)

  

  def test_random_multiple_people_punishment(self):
      # Test: Valid input 
      names = ["Rin", "Elena", "Tony", "Corrine"]
      result = random_multiple_people_punishment(2, names)
      assert isinstance(result, str), "Output should be a string"
      assert "must" in result, "Output should contain 'must'"

      # Test: Input is not a list
      result = random_multiple_people_punishment(2, "Rin, Elena, Tony")
      assert result == "Error: The name list must be a valid list.", "Should return error for non-list input"

      # Test: List with invalid entries (None, numbers, empty strings)
      result = random_multiple_people_punishment(2, ["Rin", "", None, 42])
      assert result == "Error: Please provide a list of non-empty strings.", "Should return error for invalid entries"

      # Test: Zero people to punish
      result = random_multiple_people_punishment(0, ["Rin", "Elena"])
      assert result == "Error: The number of people to punish must be at least 1.", "Should return error for zero punishments"

      # Test: More punishments than available names
      result = random_multiple_people_punishment(5, ["Rin", "Elena"])
      assert result == "Error: Cannot punish 5 people when only 2 names are available.", "Should return error for too many punishments"

      # Test: Handling duplicate names 
      result = random_multiple_people_punishment(2, ["Rin", "Rin", "Elena", "Elena"])
      assert result == "Error: Duplicate names are not allowed. Please provide unique names.", "Should return error for duplicate names"

  # Run the test if this script is executed directly
  if __name__ == "__main__":
      pytest.main()

