import __hello__; __hello__.main()
print ("God pip install python")

import time
import os
import sys
from threading import Thread
from objects import World, Lovable, PointSet, Circle, SineWave, Sequence, Eggplant, Tomato, TabbyCat, Trapped, IllegalArgumentException, sing

def play_audio(file_path):
    """Pygame을 사용하여 로컬 오디오 파일을 재생하는 함수"""

    if not os.path.exists(file_path):
        print(f"오디오 파일을 찾을 수 없습니다: {file_path}")
        print("파일 경로가 올바른지 다시 확인해주세요.")
        return

    try:
        pygame.mixer.init() # Pygame 믹서 초기화
        pygame.mixer.music.load(file_path) # 오디오 파일 로드
        pygame.mixer.music.play() # 오디오 재생
    except Exception as e:
        print(f"오디오 재생 실패: {e}")
        print("pygame 설치 확인 또는 오디오 파일 문제일 수 있습니다.")
        print(f"오류 상세: {e}")

current_code_time = 0.0
        
def srt_time_to_seconds(srt_time_str):
    """SRT 시간 문자열(HH:MM:SS,ms)을 초 단위 float으로 변환합니다."""
    parts = srt_time_str.replace(',', '.').split(':')
    h = int(parts[0])
    m = int(parts[1])
    
    
    s = float(parts[2])
    return h * 3600 + m * 60 + s

def custom_sleep_and_print(target_time, text_to_print):
    """
    현재 시간부터 목표 시간까지 sleep하고 텍스트를 출력한 후,
    현재 시간을 목표 시간으로 업데이트합니다.
    """
    global current_code_time
    sleep_duration = target_time - current_code_time
    if sleep_duration > 0:
        time.sleep(sleep_duration)
    
    if text_to_print: # 출력할 텍스트가 있을 경우에만 출력
        print(text_to_print)
    current_code_time = target_time # 현재 시간을 목표 시간으로 업데이트

def main():
    global current_code_time # 전역 current_code_time 사용
    """
    이 프로그램은 의미나 목적이 없는
    텅 빈 시뮬레이션 세계를 만듭니다.
    """
    
    # [cite_start]0:00:02,920 --> 0:00:03,873 PROTECTION [cite: 1]
    custom_sleep_and_print(srt_time_to_seconds("00:00:00,100"), "Switch on the power line")

    custom_sleep_and_print(srt_time_to_seconds("00:00:01,740"), "Remember to put on")
    
    # [cite_start]0:00:02,920 --> 0:00:03,873 PROTECTION [cite: 1]
    custom_sleep_and_print(srt_time_to_seconds("00:00:02,920"), "PROTECTION")

    # [cite_start]00:00:03,873 --> 00:00:05,491 Lay down your pieces [cite: 1]
    custom_sleep_and_print(srt_time_to_seconds("00:00:03,873"), "Lay down your pieces")

    # [cite_start]00:00:05,491 --> 00:00:06,380 And let's begin [cite: 1]
    custom_sleep_and_print(srt_time_to_seconds("00:00:05,491"), "And let's begin")
    
    # [cite_start]0:00:06,380 --> 0:00:07,446 OBJECT CREATION [cite: 1]
    world = World() # World 인스턴스 미리 생성
    me = Lovable("Me", 0, True, -1, False) # Lovable 인스턴스 미리 생성
    you = Lovable("You", 0, True, -1, False) # Lovable 인스턴스 미리 생성
    custom_sleep_and_print(srt_time_to_seconds("00:00:06,380"), "OBJECT CREATION")

    # [cite_start]00:00:07,446 --> 00:00:10,091 Fill in my data parameters [cite: 1]
    custom_sleep_and_print(srt_time_to_seconds("00:00:07,446"), "Fill in my data parameters")

    # [cite_start]0:00:10,091 --> 0:00:11,095 INITIALIZATION [cite: 1]
    custom_sleep_and_print(srt_time_to_seconds("00:00:10,091"), "INITIALIZATION")
    
    # [cite_start]0:00:11,095 --> 0:00:12,906 Set up our new world [cite: 1]
    world.add_thing(me)
    world.add_thing(you)
    custom_sleep_and_print(srt_time_to_seconds("00:00:11,095"), "Set up our new world")

    # [cite_start]0:00:13,891 --> 0:00:14,888 SIMULATION [cite: 1]
    world.start_simulation()
    custom_sleep_and_print(srt_time_to_seconds("00:00:13,891"), "THE SIMULATION")
    
    # [cite_start]0:00:16,000 --> 0:00:23,080 world.execute(me); [cite: 2]
    custom_sleep_and_print(srt_time_to_seconds("00:00:16,000"), "world.execute(me);")

    # [cite_start]0:00:29,709 --> 0:00:33,412 If I'm a set of points, Then I will give you my DIMENSION [cite: 2]
    custom_sleep_and_print(srt_time_to_seconds("00:00:29,709"), None) # 다음 대사까지의 빈 시간 (대기)
    if isinstance(me, PointSet):
        you.add_attribute(me.get_dimensions().to_attribute())
    custom_sleep_and_print(srt_time_to_seconds("00:00:29,709"), "\n\nIf I'm a set of points, Then I will give you my dimension")

    # [cite_start]0:00:33,412 --> 0:00:37,067 If I'm a circle, Then I will give you my CIRCUMFERENCE [cite: 2]
    if isinstance(me, Circle):
        you.add_attribute(me.get_circumference().to_attribute())
    custom_sleep_and_print(srt_time_to_seconds("00:00:33,412"), "If I'm a circle, Then I will give you my circumference")

    # [cite_start]0:00:37,067 --> 0:00:40,706 If I’m a sine wave, Then you can sit on all my TANGENTS [cite: 2]
    if isinstance(me, SineWave):
        you.add_action("sit", me.get_tangent(you.get_x_position()))
    custom_sleep_and_print(srt_time_to_seconds("00:00:37,067"), "If I'm a sine wave, Then you can sit on all my tangents")

    # [cite_start]0:00:40,706 --> 0:00:44,452 If I approach infinity, Then you can be my LIMITATIONS [cite: 2]
    if isinstance(me, Sequence):
        me.set_limit(you.to_limit())
    custom_sleep_and_print(srt_time_to_seconds("00:00:40,706"), "If I approach infinity, then you can be MY LIMITATIONS")

    # [cite_start]0:00:44,452 --> 0:00:47,672 Switch my current To AC to DC [cite: 2]
    me.toggle_current()
    custom_sleep_and_print(srt_time_to_seconds("00:00:44,452"), "\nSwitch my current To AC to DC")

    # [cite_start]0:00:47,672 --> 0:00:51,363 And then blind my vision, So dizzy so dizzy [cite: 2]
    me.can_see = False
    me.add_feeling("dizzy")
    custom_sleep_and_print(srt_time_to_seconds("00:00:47,672"), "And then blind my vision, So dizzy, so dizzy")

    # [cite_start]0:00:51,363 --> 0:00:55,083 Oh we can travel To A.D to B.C [cite: 2]
    world.time_travel_for_two("AD", 617, me, you)
    world.time_travel_for_two("BC", 3691, me, you)
    custom_sleep_and_print(srt_time_to_seconds("00:00:51,363"), "Oh, we can travel From A.D to B.C")

    # [cite_start]0:00:55,083 --> 0:00:59,223 And we can unite So deeply so deeply [cite: 2]
    world.unite(me, you)
    custom_sleep_and_print(srt_time_to_seconds("00:00:55,083"), "And we can unite So deeply, so deeply")

    # [cite_start]0:00:59,223 --> 0:01:06,601 If I can, If I can, give you all the STIMULATIONS, Then I can, Then I can, be your only SATISFACTION [cite: 3]
    if (me.get_simulations_available()) >= (you.get_num_simulations_needed()):
        you.set_satisfaction(me.to_satisfaction())
    custom_sleep_and_print(srt_time_to_seconds("00:00:59,223"), "\nIf I can, If I can, give you all THE SIMULATIONS, Then I can, Then I can, be your only SATISFACTION")

    # [cite_start]0:01:06,601 --> 0:01:10,084 If I can make you happy, I will run the EXECUTION [cite: 3]
    if (you.get_feeling_index("happy") != -1):
        me.request_execution(me)
    custom_sleep_and_print(srt_time_to_seconds("00:01:06,601"), "If I can make you happy, Then I'll run the EXECUTION")

    # [cite_start]0:01:10,084 --> 0:01:14,045 Though we are trapped In this strange strange SIMULATION [cite: 3]
    world.lock_thing(me)
    world.lock_thing(you)
    custom_sleep_and_print(srt_time_to_seconds("00:01:10,084"), "Though we are trapped In this strange, strange SIMULATION")
    
    # [cite_start]0:01:14,045 --> 0:01:17,576 If I'm an eggplant, Then I will give you my NUTRIENTS [cite: 3]
    if isinstance(me, Eggplant):
        you.add_attribute(me.get_nutrients().to_attribute())
    custom_sleep_and_print(srt_time_to_seconds("00:01:14,045"), "\nIf I'm an eggplant, Then I will give you my NUTRIENTS")

    # [cite_start]0:01:17,576 --> 0:01:21,351 If I'm a tomato, Then I will give you ANTIOXIDANTS [cite: 3]
    if isinstance(me, Tomato):
        you.add_attribute(me.get_antioxidants().to_attribute())
    custom_sleep_and_print(srt_time_to_seconds("00:01:17,576"), "If I'm a tomato, Then I'll give you ANTIOXIDANTS")

    # [cite_start]0:01:21,351 --> 0:01:25,078 If I'm a tabby cat, Then I will purr for your ENJOYMENT [cite: 3]
    if isinstance(me, TabbyCat):
        pass # MockObject handles this
    custom_sleep_and_print(srt_time_to_seconds("00:01:21,351"), "If I'm a tabby cat, Then I will purr for your ENJOYMENT")

    # [cite_start]0:01:25,078 --> 0:01:28,587 If I’m the only god, Then you're the proof of my EXISTENCE [cite: 4]
    if world.get_god().equals(me):
        me.set_proof(you.to_proof())
    custom_sleep_and_print(srt_time_to_seconds("00:01:25,078"), "If I'm the only god, Then your the proof of my EXISTENCE")

    # [cite_start]0:01:28,587 --> 0:01:32,015 Switch my gender To F to M [cite: 4]
    me.toggle_gender()
    custom_sleep_and_print(srt_time_to_seconds("00:01:28,587"), "\nSwitch my gender To F to M")

    # [cite_start]0:01:32,015 --> 0:01:35,465 And then do whatever From AM to PM [cite: 4]
    world.procreate(me, you)
    custom_sleep_and_print(srt_time_to_seconds("00:01:32,015"), "And then do whatever From AM to PM")

    # [cite_start]0:01:35,465 --> 0:01:39,349 Oh switch my role To S to M [cite: 4]
    me.toggle_role_bdsm()
    custom_sleep_and_print(srt_time_to_seconds("00:01:35,465"), "I will switch my role To S to M")

    # [cite_start]0:01:39,349 --> 0:01:43,489 So we can enter The trance the trance [cite: 4]
    world.make_high(me)
    world.make_high(you)
    custom_sleep_and_print(srt_time_to_seconds("00:01:39,349"), "So we can enter The trance, the trance")

    # [cite_start]0:01:43,489 --> 0:01:50,900 If I can, If I can, feel your VIBRATIONS, Then I can, Then I can, finally be COMPLETION [cite: 4]
    if me.get_sense_index("vibration"):
        me.add_feeling("complete")
    custom_sleep_and_print(srt_time_to_seconds("00:01:43,489"), "\nIf I can, If I can, feel your VIBRATIONS, Then I can, Then I can, finally be COMPLETION")

    # [cite_start]0:01:50,900 --> 0:01:52,220 Though you have left [cite: 4]
    world.unlock(you)
    world.remove_thing(you)
    custom_sleep_and_print(srt_time_to_seconds("00:01:50,900"), "Though you have left")

    # [cite_start]0:01:52,220 --> 0:01:53,100 You have left [cite: 4]
    me.look_for(you, world)
    custom_sleep_and_print(srt_time_to_seconds("00:01:52,220"), "You have left")

    # [cite_start]0:01:53,100 --> 0:01:54,180 You have left [cite: 4]
    me.look_for(you, world)
    custom_sleep_and_print(srt_time_to_seconds("00:01:53,100"), "You have left")

    # [cite_start]0:01:54,180 --> 0:02:54,920 You have left [cite: 4]
    me.look_for(you, world)
    custom_sleep_and_print(srt_time_to_seconds("00:01:54,180"), "You have left")

    # [cite_start]0:01:54,920 --> 0:01:58,333 You have left me in ISOLATION [cite: 4, 5]
    me.look_for(you, world)
    custom_sleep_and_print(srt_time_to_seconds("00:01:54,920"), "You have left me in ISOLATION")

    # [cite_start]0:01:58,333 --> 0:02:05,708 If I can, If I can, erase all the pointless FRAGMENTS, Then maybe, Then maybe, you won't leave me so DISHEARTENED [cite: 5]
    if me.get_memory().is_erasable():
        me.remove_feeling("disheartened")
    custom_sleep_and_print(srt_time_to_seconds("00:01:58,333"), "If I can, If I can, erase all the pointless FRAGMENTS, Then maybe, Then maybe, you won't leave me so DISHEARTENED")

    # [cite_start]0:02:05,708 --> 0:02:13,612 Challenging your god, You have made some ILLEGAL ARGUMENTS [cite: 5]
    try:
        me.set_opinion(me.get_opinion_index("you are here"), False)
    except IllegalArgumentException:
        world.announce("God is always true.")
    custom_sleep_and_print(srt_time_to_seconds("00:02:05,708"), "Challenging your god, You have made some ILLEGAL ARGUMENTS")
    
    # EXECUTION Loop and Numbers (SRT 87-98, then 99-105)
    # [cite_start]0:02:27,660 --> 0:02:28,560 EXECUTION [cite: 5]
    custom_sleep_and_print(srt_time_to_seconds("00:02:27,660"), "\n\nEXECUTION")
    # [cite_start]0:02:28,600 --> 0:02:29,440 EXECUTION [cite: 5]
    custom_sleep_and_print(srt_time_to_seconds("00:02:28,600"), "EXECUTION")
    # [cite_start]0:02:29,520 --> 0:02:30,460 EXECUTION [cite: 5]
    custom_sleep_and_print(srt_time_to_seconds("00:02:29,520"), "EXECUTION")
    # [cite_start]0:02:30,540 --> 0:02:31,400 EXECUTION [cite: 5]
    custom_sleep_and_print(srt_time_to_seconds("00:02:30,540"), "EXECUTION")
    # [cite_start]0:02:31,520 --> 0:02:32,180 EXECUTION [cite: 5]
    custom_sleep_and_print(srt_time_to_seconds("00:02:31,520"), "EXECUTION")
    # [cite_start]0:02:32,280 --> 0:02:33,100 EXECUTION [cite: 5]
    custom_sleep_and_print(srt_time_to_seconds("00:02:32,280"), "EXECUTION")
    # [cite_start]0:02:33,160 --> 0:02:33,900 EXECUTION [cite: 5]
    custom_sleep_and_print(srt_time_to_seconds("00:02:33,160"), "EXECUTION")
    # [cite_start]0:02:33,980 --> 0:02:35,120 EXECUTION [cite: 5]
    custom_sleep_and_print(srt_time_to_seconds("00:02:33,980"), "EXECUTION")
    # [cite_start]0:02:35,200 --> 0:02:36,020 EXECUTION [cite: 5]
    custom_sleep_and_print(srt_time_to_seconds("00:02:35,200"), "EXECUTION")
    # [cite_start]0:02:36,080 --> 0:02:36,960 EXECUTION [cite: 5]
    custom_sleep_and_print(srt_time_to_seconds("00:02:36,080"), "EXECUTION")
    # [cite_start]0:02:37,040 --> 0:02:37,920 EXECUTION [cite: 5]
    custom_sleep_and_print(srt_time_to_seconds("00:02:37,040"), "EXECUTION")
    # [cite_start]0:02:38,000 --> 0:02:38,800 EXECUTION [cite: 5]
    custom_sleep_and_print(srt_time_to_seconds("00:02:38,000"), "EXECUTION")

    # Numbers
    # [cite_start]0:02:38,900 --> 0:02:39,321 EIN [cite: 5]
    world.announce("1", "de") # ein; German
    custom_sleep_and_print(srt_time_to_seconds("00:02:38,900"), "Ein")
    # [cite_start]0:02:39,321 --> 0:02:39,657 DOS [cite: 5]
    world.announce("2", "es") # dos; Español
    custom_sleep_and_print(srt_time_to_seconds("00:02:39,321"), "Dos")
    # [cite_start]0:02:39,657 --> 0:02:40,244 TROIS [cite: 5]
    world.announce("3", "fr") # trois; French
    custom_sleep_and_print(srt_time_to_seconds("00:02:39,657"), "Trois")
    # [cite_start]0:02:40,244 --> 0:02:40,693 NE [cite: 5]
    world.announce("4", "kr") # 넷; Korean
    custom_sleep_and_print(srt_time_to_seconds("00:02:40,244"), "Ne")
    # [cite_start]0:02:40,693 --> 0:02:41,124 FEM [cite: 5]
    world.announce("5", "se") # fem; Swedish
    custom_sleep_and_print(srt_time_to_seconds("00:02:40,693"), "Fem")
    # [cite_start]0:02:41,124 --> 0:02:41,584 LIU [cite: 5]
    world.announce("6", "cn") # 六; Chinese
    custom_sleep_and_print(srt_time_to_seconds("00:02:41,124"), "Liu")
    
    # [cite_start]0:02:41,584 --> 0:02:42,632 EXECUTION [cite: 5]
    world.run_execution()
    custom_sleep_and_print(srt_time_to_seconds("00:02:41,584"), "EXECUTION")

    # [cite_start]0:02:42,632 --> 0:02:49,824 If I can, If I can, give you all the EXECUTION, Then I can, Then I can, be your only EXECUTION [cite: 6]
    if world.is_executable_by(me):
        you.set_execution(me.to_execution())
    custom_sleep_and_print(srt_time_to_seconds("00:02:42,632"), "\nIf I can, If I can, give you all the EXECUTION, Then I can, Then I can, be your only EXECUTION")

    # [cite_start]0:02:49,824 --> 0:02:53,643 If I can have you back, I will run the EXECUTION [cite: 6]
    if (world.get_thing_index(you) != -1):
        world.run_execution()
    custom_sleep_and_print(srt_time_to_seconds("00:02:49,824"), "If I can, have you back, Then I will run the EXECUTION")
    
    # [cite_start]0:02:53,643 --> 0:02:57,246 Though we are trapped, We are trapped ah [cite: 6]
    me.escape(world)
    custom_sleep_and_print(srt_time_to_seconds("00:02:53,643"), "Though we are trapped, We are trapped ah")

    # [cite_start]0:02:57,246 --> 0:03:00,857 I've studied, I've studied how to properly LO-O-OVE [cite: 6]
    me.learn_topic("love")
    custom_sleep_and_print(srt_time_to_seconds("00:02:57,246"), "I've studied, I've studied how to properly LO-O-OVE")

    # [cite_start]0:03:00,857 --> 0:03:04,540 Question me, Question me I can answer all LO-O-OVE [cite: 6]
    me.take_exam_topic("love")
    custom_sleep_and_print(srt_time_to_seconds("00:03:00,857"), "Question me, Question me I can answer all LO-O-OVE")

    # [cite_start]0:03:04,540 --> 0:03:08,483 I know the algebraic expression of LO-O-OVE [cite: 6]
    me.get_algebraic_expression("love")
    custom_sleep_and_print(srt_time_to_seconds("00:03:04,540"), "I know the algebraic expression of LO-O-OVE")

    # [cite_start]0:03:08,483 --> 0:03:12,160 Though you are free, I am trapped, trapped in LO-O-OVE [cite: 6]
    try:
        me.escape("love")
    except Trapped:
        world.execute(me)
    custom_sleep_and_print(srt_time_to_seconds("00:03:08,483"), "Though you are free, I am trapped, trapped in LO-O-OVE")

    # [cite_start]0:03:25,811 --> 0:03:27,060 EXECUTION [cite: 6]
    custom_sleep_and_print(srt_time_to_seconds("00:03:25,811"), "\n\nEXECUTION")

if __name__ == '__main__':
    # 오디오 재생을 별도의 스레드에서 시작
    # mp3 파일은 별도로 구하시길 바랍니다.
    # ----------------------------------------------------------------------
    audio_file_path = r"(your_path)"
    audio_thread = Thread(target=play_audio, args=(audio_file_path,))
    audio_thread.daemon = True # 메인 스레드 종료 시 오디오 스레드도 함께 종료
    audio_thread.start()

    main()
time.sleep(3)
sys.exit
