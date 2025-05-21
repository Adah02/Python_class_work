#Nokia 3310 Menu Operations
while True:
  print("""
   List of Menu functions
    Press;-
  1 > Phone book
  2 > Messages
  3 > Chat
  4 > Call register
  5 > Tones
  6 > Settings
  7 > Call divert
  8 > Games
  9 > Calculator
  10 > Reminder
  11 > Clock
  12 > Profiles
  13 > SIM services
   0 > Back
   """)
  user_input = input("Enter selection: ")
  match user_input:
    case "1":
      while True:
        print("""
         Phone Book
	  Press;-
	 1 > Search
	 2 > Service Nos
	 3 > Add name
	 4 > Erase
	 5 > Edit
	 6 > Assign tone
	 7 > Send b'card
	 8 > Options
	 9 > Speed dials
	 10 > Voice tags
          0 > Back	
	 """)
        phone_book_select = input("Enter selection: ")
        match phone_book_select:
          case "1":
            while True:
              print("Search")
              search = input("Press 0 > Back: ")
              if search == "0":
                break         
          case "2":
            while True:
              print("Service Nos")
              service = input("Press 0 > Back: ")
              if service == "0":
                break
          case "3":
            while True:
              print("Add name")
              add_name = input("Press 0 > Back: ")
              if add_name == "0":
                break
          case "4":
            while True:
              print("Erase")
              erase = input("Press 0 > Back: ")
              if erase == "0":
                break
          case "5":
            while True:
              print("Edit")
              edit = input("Press 0 > Back: ")
              if edit == "0":
                break
          case "6":
            while True:
              print("Assign tone")
              assign_ = input("Press 0 > Back: ")
              if assign_ == "0":
                break
          case "7":
            while True:
              print("Send b'card")
              send_card = input("Press 0 > Back: ")
              if send_card == "0":
                break
          case "8":
            while True:
              print("""
		Options
		  Press;- 
		1 > Type of view
		2 > Memory status
                0 > Back
	         """)
              option_select = input('Enter selection: ')
              match option_select:
                case "1":
                  while true:
                    print("Type of view")
                    view = input("Press 0 > Back: ")
                    if view == "0":
                        break
                case "2":
                  while true:
                    print("Memory status")
                    status = input("Press 0 > Back: ")
                    if status == "0":
                      break                 
          case "9":
            while True:
              print("Speed dials")
              speed = input("Press 0 > Back: ")
              if speed == 0:
                break
          case "10":
            while True:
              print("Voice tags")
              tags = input("Press 0 > Back: ")
              if tags == "0":
                break
          case _: 
            break
    case "2":
      while True:
        print("""
	      Messages
	       Press;-
	     1 > Write messages
	     2 > Inbox
	     3 > Outbox
	     4 > Picture message
	     5 > Templates
	     6 > Smileys
	     7 > Message settings
	     8 > Info service
	     9 > Voice mailbox number
	    10 > Service command editor
	     0 > Back
	""")
        messages = input("Enter selection: ")
        match messages:
          case "1":
            while True:
              print("Write messages")
              write = input("Press 0 > Back: ")
              if write == "0":
                break
          case "2":
            while True:
              print("Inbox")
              inbox = input('Press 0 > Back: ')
              if inbox == "0":
                break
          case "3":
            while True:
              print("Outbox")
              outbox = input('Press 0 > Back: ')
              if outbox == "0":
                break
          case "4":
            while True:
              print("Picture message")
              picture = input('Press 0 > Back: ')
              if picture == "0":
                break
          case "5":
            while True:
              print("Templates")
              templates = input('Press 0 > Back: ')
              if templates == "0":
                break
          case "6":
            while True:
              print("Smileys")
              smileys = input('Press 0 > Back: ')
              if smileys == "0":
                break
          case "7":
            while True:
              print("""
		Message settings
		Press;-
		1 > Set
		2 > Common
                0 > Back
		""")
              message_settings = input('Enter selection: ')
              match message_settings:
                case "1":
                  while True:
                    print(""" 
		        Set
		        Press;-
		       1 > Message centre number
		       2 > Message sent as
		       3 > Message validity
                       0 > Back
		     """)
                    set_1 = input('Enter selection: ')
                    match set_1:
                      case "1": 
                        while True:
                          print("Message centre number")
                          message_number = input("Press 0 > Back: ")
                          if message_number == "0":
                            break
                      case "2":
                        while True:
                          print("Message sent as")
                          message_sent = input("Press 0 > Back: ")
                          if message_sent == "0":
                            break
                      case "3":
                        while True:
                         print("Message validity")
                         message_validity = input("Press 0 > Back: ")
                         if message_validity == "0":
                           break
                case "2":
                  while True:
                    print("""
			Press;- 
			1 > Delivery reports
			2 > Reply via same centre
			3 > Character support
                        0 > Back
                    """)
                    common = input("Enter selection: ")
                    match common:
                      case "1":
                        while True:
                          print("Delivery report")
                          delivery_report = input("Press 0 > Back: ")
                          if delivery_report == "0":
                            break
                      case "2":
                        while True:
                          print("Reply via same centre")
                          same_centre = input("Press 0 > Back: ")
                          if same_centre == "0":
                            break
                      case "3":
                        while True:
                          print("Character support")
                          character_support = input("Press 0 > Back: ")
                          if character_support == "0":
                            break  
          case "8":
            while True:
              print("Info service")
              info_service = input("Press 0 > Back: ")
              if info_service == "0":
                break
          case "9":
            while True:
              print("Voice mailbox number")
              mailbox_number = input("Press 0 > Back: ")
              if mailbox_number == "0":
                break
          case "10":
            while True:
              print("Service command editor")
              command_editor = input("Press 0 > Back: ")
              if command_editor == "0":
                break

    case "3":
      while True:
        print("Chat")
        chat = print(input('Press 0 > Back: '))
        if chat == "0":
          break
    case "4":
      while True:
        print("""
		Call Register
		Press;- 
		1 > Missed calls
		2 > Received calls
		3 > Dialled numbers
		4 > Erase recent call list
		5 > Show call duration
		6 > Show call cost
		7 > Call cost settings
		8 > Prepaid credit
                0 > Bcak
               """)
        call_register = input("Enter selection: ")
        match call_register:
          case "1":
            while True:
              print("Missed calls")
              missed_calls = input("Press 0 > Back: ")
              if missed_calls == "0":
                break  
          case "2": 
            while True:
              print("Received calls")
              received_calls = input("Press 0 > Back: ")
              if received_calls == "0":
                break 
          case "3":
            while True:
              print("Dialled numbers")
              dialled_numbers = input("Press 0 > Back: ")
              if dialled_numbers == "0":
                break 
          case "4":
            while True:
              print("Erase recent call list")
              call_list = input("Press 0 > Back: ")
              if call_list == "0":
                break 
          case "5":
            while True:
              print("""
		Show call duration
		Press;- 
		1 > Last call duration
		2 > All calls' duration
		3 > Received calls' duration
		4 > Dialled calls' duration
		5 > Clear timer
                0 > Back
		""")
              call_duration = input("Enter selection")	
              match call_duration:
                case "1":
                  while True:
                    print("Last call duration")
                    last_call = input("Press 0 > Back: ")
                    if last_call == "0":
                      break
                case "2":
                  while True:
                    print("All calls' duration")
                    all_calls = input("Press 0 > Back: ")
                    if all_calls == "0":
                      break
                case "3":
                  while True:
                    print("Received calls' duration")
                    calls_duration = input("Press 0 > Back: ")
                    if calls_duration == "0":
                      break
                case "4":
                  while True:
                    print("Dialled calls' duration")
                    dialled_calls = input("Press 0 > Back: ")
                    if dialled_calls == "0":
                      break
                case "5":
                  while True:
                    print("Clear timer")
                    clear_timer = input("Press 0 > Back: ")
                    if clear_timer == "0":
                      break
          case "6":
            while True:
              print("""
                Show call cost
                 Press;- 
               1 > Call cost settings
               2 > All calls' cost
               3 > Clear counters
               0 > Back
               """)
            call_cost = input("Enter selection")
            match call_cost:
              case "1":
                while True:
                  print("Call cost settings")
                  cost_settings = input("Press 0 > Back: ")
                  if cost_settings == "0":
                    break
              case "2":
                while True:
                  print("All calls' cost")
                  all_calls = input("Press 0 > Back: ")
                  if all_calls == "0":
                    break
              case "3":
                while True:
                  print("Clear counters")
                  clear_counter = input("Press 0 > Back: ")
                  if clear_counter == "0":
                    break
          case "7": 
            while True:
              print("""
		Call cost settings
		Press;- 
		1 > Call cost limit
		2 > Show costs in 
                0 > Back
		""")
              cost_settings = input("Enter selection")
              match cost_settings:
                case "1":
                  while True:
                    print("Call cost limit")
                    cost_limit = input("Press 0 > Back: ")
                    if cost_limit == "0":
                      break
                case "2":
                  while True:
                    print("Show costs in")
                    show_cost = input("Press 0 > Back: ")
                    if show_cost == "0":
                      break
          case "8":
            while True:
              print("Prepaid")
              prepaid = input("Press 0 > Back: ")
              if prepaid == "0":
                break
    case "5":
      while True:
        print("""
		Tones
		Press;- 
		1 > Ringing tone
		2 > Ringing volume
		3 > Incoming call alert
		4 > Composer
		5 > Message alert tone
		6 > Keypad tones
		7 > Warning and game tones
		8 > Vibrating alert
		9 > Screen saver
                0 > Back
	      """)
        tones = input('Enter selection: ')
        match tones:
          case "1":
            while True:
              print("Ringing tone")
              ringing_tone = input("Press 0 > Back: ")
              if ringing_tone == "0":
                break
          case "2":
            while True:
              print("Ringing volume")
              ringing_volume = input("Press 0 > Back: ")
              if ringing_volume == "0":
                break
          case "3":
            while True:
              print("Incoming call alert")
              call_alert = input("Press 0 > Back: ")
              if call_alert == "0":
                break
          case "4":
            while True:
              print("Composer")
              composer = input("Press 0 > Back: ")
              if composer == "0":
                break
          case "5":
            while True:
              print("Message alert tone")
              alert_tone = input("Press 0 > Back: ")
              if alert_tone == "0":
                break
          case "6":
            while True:
              print("Keypad tones")
              keypad_tones = input("Press 0 > Back: ")
              if keypad_tones == "0":
                break
          case "7":
            while True:
              print("Warning and game tones")
              game_tone = input("Press 0 > Back: ")
              if game_tone == "0":
                break
          case "8":
            while True:
              print("Vibrating alert")
              vibrating = input("Press 0 > Back: ")
              if vibrating == "0":
                break
          case "9":
            while True:
              print("Screen saver")
              screen_saver = input("Press 0 > Back: ")
              if screen_saver == "0":
                break
          case _:
            break
    case "6":
      while True:
        print("""
          Ssttings
           Press;- 
	  1 > Call settings			
	  2 > Phone settings
	  3 > Security settings
	  4 > Restore factory settings
	  0 > Back
	  """)
        settings = input("Enter selection: ")
        match settings:
          case "1":
            while True:
              print("""
		Call settings
		Press;- 
		1 > Automatic redial
		2 > Speed dialing
		3 > Call waiting options
		4 > Own number sending
		5 > Phone number in use
		6 > Automatic answer
		0 > Back
                """)
              call_settings = input("Enter selection: ")
              match call_settings:
                case "1":
                  while True:
                    print("Automatic redial")
                    automatic_redial = input("Press 0 > Back: ")
                    if automatic_redial == "0":
                      break
                case "2":
                  while True:
                    print("Speed dialing")
                    speed_dialing = input("Press 0 > Back: ")
                    if speed_dialing == "0":
                      break
                case "3":
                  while True:
                    print("Call waiting options")
                    call_waiting = input("Press 0 > Back: ")
                    if call_waiting == "0":
                      break
                case "4":
                  while True:
                    print("Own number sending")
                    own_number = input("Press 0 > Back: ")
                    if own_number == "0":
                      break
                case "5":
                  while True:
                    print("Phone number in use")
                    phone_number = input("Press 0 > Back: ")
                    if phone_number == "0":
                      break
                case "6":
                  while True:
                    print("Automatic answer")
                    automatic_answer = input("Press 0 > Back: ")
                    if automatic_answer == "0":
                      break
                case _:
                  break
          case "2":
            while True:
              print("""
		Phone settings
		Press;- 
		1 > Language
		2 > Call info display
		3 > Welcome note
		4 > Network selection
		5 > Lights
		6 > Confirm SIM service actions
		0 > Back
		""")
              phone_settings = input("Enter selection: ")
              match phone_settings:
                case "1":
                  while True:
                    print("Language")
                    language = input("Press 0 > Back: ")
                    if language == "0":
                      break
                case "2":
                  while True:
                    print("Call info display")
                    info_display = input("Press 0 > Back: ")
                    if info_display == "0":
                      break
                case "3":
                  while True:
                    print("Welcome note")
                    welcome_note = input("Press 0 > Back: ")
                    if welcome_note == "0":
                      break
                case "4":
                  while True:
                    print("Network selection")
                    network = input("Press 0 > Back: ")
                    if network == "0":
                      break
                case "5":
                  while True:
                    print("Lights")
                    lights = input("Press 0 > Back: ")
                    if lights == "0":
                      break
                case "6":
                  while True:
                    print("Confirm SIM service actions")
                    sim_service = input("Press 0 > Back: ")
                    if sim_service == "0":
                      break
                case _:
                  break
          case 3:
            while True:
              print("""
		Security settings
		Press;- 
		1 > PIN code request
		2 > Call barring service
		3 > Fixed dialing
		4 > Closed user group
		5 > Phone security
		6 > Change access codes
                0 > Back
		""")
              security_settings = input("Enter slection: ")
              match security_settings:
                case "1":
                  while True:
                    print("PIN code request")
                    pin_code = input("Press 0 > Back: ")
                    if pin_code == "0":
                      break
                case "2":
                  while True:
                    print("Call barring service")
                    call_barring = input("Press 0 > Back: ")
                    if call_barring == "0":
                      break
                case "3":
                  while True:
                    print("Fixed dialing")
                    fixed_dialing = input("Press 0 > Back: ")
                    if fixed_dialing == "0":
                      break
                case "4":
                  while True:
                    print("Closed user group")
                    closed_user = input("Press 0 > Back: ")
                    if closed_user == "0":
                      break
                case "5":
                  while True:
                    print("Phone security")
                    phone_security = input("Press 0 > Back: ")
                    if phone_security == "0":
                      break
                case "6":
                  while True:
                    print("Change access codes")
                    access_codes = input("Press 0 > Back: ")
                    if access_codes == "0":
                      break
                case _: 
                  break
          case "4":
            while True:
              print("Restore factory settings")
              factory_settings = input("Press 0 > Back: ")
              if factory_settings == "0":
                break
          case _:
            break
    case "7":
      while True:
        print("Call divert")
        call_divert = input("Press 0 > Back: ")
        if call_divert == "0":
          break
    case "8":
      while True:
        print("Game")
        games = input("Press 0 > Back: ")
        if games == "0":
          break
    case "9":
      while True:
        print("Calculator")
        calculator = input("Press 0 > Back: ")
        if calculator == "0":
          break
    case "10":
      while True:
        print("Reminder")
        reminder = input("Press 0 > Back: ")
        if reminder == "0":
          break
    case "11":
      while True:
        print("""
	  Clock
	  Press;- 
	  1 > Alarm clock
	  2 > Clock settings
	  3 > Date settings
	  4 > Stopwatch
	  5 > Countdown timer
    	  6 > Auto update of date and time
	  0 > Back    
          """)
        clock = print("Enter selection: ")
        match clock:
          case "1":
            while True:
              print("Alarm clock")
              alarm = input("Press 0 > Back: ")
              if alarm == "0":
                break
          case "2":
            while True:
              print("Clock settings")
              clock_settings = input("Press 0 > Back: ")
              if clock_settings == "0":
                break
          case "3":
            while True:
              print("Date settings")
              date_settings = input("Press 0 > Back: ")
              if date_settings == "0":
                break
          case "4":
            while True:
              print("Stopwatch")
              stopwatch = input("Press 0 > Back: ")
              if stopwatch == "0":
                break
          case "5":
            while True:
              print("Countdown timer")
              count = input("Press 0 > Back: ")
              if count == "0":
                break
          case "6":
            while True:
              print("Auto update of date and time")
              auto_update = input("Press 0 > Back: ")
              if auto_update == "0":
                break
          case _:
            break

    case "12":
      while True:
        print("Profiles")
        profiles = input("Press 0 > Back: ")
        if profiles == "0":
          break
    case "13":
      while True:
        print("SIM Services")
        sim_services = input("Press 0 > Back: ")
        if sim_services == "0":
          break
