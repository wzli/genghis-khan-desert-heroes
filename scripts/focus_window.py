#!/usr/bin/env python3
import time
import subprocess

def raise_game_window():
    try:
        from Xlib import display, X, protocol
        d = display.Display()
        d.set_error_handler(lambda *args, **kwargs: None)
        root = d.screen().root
        atom_active = d.intern_atom("_NET_ACTIVE_WINDOW")
        atom_state = d.intern_atom("_NET_WM_STATE")
        atom_above = d.intern_atom("_NET_WM_STATE_ABOVE")

        for _ in range(50):
            time.sleep(0.15)
            try:
                out = subprocess.check_output(["xwininfo", "-root", "-tree"], stderr=subprocess.DEVNULL).decode("latin-1", "ignore")
            except Exception:
                continue

            for line in out.splitlines():
                lower = line.lower()
                if "hero.exe" in lower or "大漠英雄" in lower or "genghiskhan" in lower or "¦¨¦n" in lower:
                    parts = line.strip().split()
                    if parts and parts[0].startswith("0x"):
                        try:
                            wid = int(parts[0], 16)
                            win = d.create_resource_object("window", wid)
                            geom = win.get_geometry()
                            if geom.width >= 400 and geom.height >= 300:
                                # Direct X11 map, raise, and input focus
                                try:
                                    win.map()
                                    win.configure(stack_mode=X.Above)
                                    win.set_input_focus(X.RevertToParent, X.CurrentTime)
                                except Exception:
                                    pass

                                # 1. Pin above other windows (_NET_WM_STATE_ABOVE) via EWMH
                                ev_above = protocol.event.ClientMessage(
                                    window=wid,
                                    client_type=atom_state,
                                    data=(32, [1, atom_above, 0, 1, 0])
                                )
                                root.send_event(ev_above, event_mask=X.SubstructureRedirectMask | X.SubstructureNotifyMask)

                                # 2. Request active focus via EWMH
                                ev_act = protocol.event.ClientMessage(
                                    window=wid,
                                    client_type=atom_active,
                                    data=(32, [2, X.CurrentTime, 0, 0, 0])
                                )
                                root.send_event(ev_act, event_mask=X.SubstructureRedirectMask | X.SubstructureNotifyMask)

                                d.sync()
                                return
                        except Exception:
                            pass
    except Exception:
        pass

if __name__ == "__main__":
    raise_game_window()


