import data, screen, sounds, logic
from clge import DefaultAssets as da

info = data.get_data()
scr = screen.open_screen(info["field_width"] + 1,
                         info["field_height"] + 1,
                         info["default_symbol"],
                         info["timeout_duration"],
                         info["auto_timeout"],
                         info["auto_clear_objects"],
                         info["default_color"])

player = da.SamplePlayer(info["player"]["begin_x"],
                         info["player"]["begin_y"],
                         info["player"]["step"],
                         info["player"]["lives"],
                         info["player"]["symbol"])

fruit = da.SampleObject(logic.fruit_first_pos_x(info["field_width"]),
                         logic.fruit_first_pos_y(info["field_height"]),
                         step=1,
                         symbol=info["fruit"]["symbol"])

while True:
    scr.clear_screen()
    logic.move(player, info["field_width"], info["field_height"], info["sound_enabled"])
    info["score"] = logic.check_collision_and_add_points(
                                                         player,
                                                         fruit,
                                                         info["score"],
                                                         {
                                                            "width": info["field_width"],
                                                            "height": info["field_height"]
                                                        })
    player.add_to_screen(scr)
    fruit.add_to_screen(scr)
    print(info["title"])
    scr.render()
    print("Score: {}".format(info["score"]))
    scr.do_timeout()
