# Force client-side decorations for apps that support them.
# GTK apps (firefox, etc.) get titlebar buttons via CSD.
# Qt apps (konsole, dolphin, kate) use CSD when WM has no SSD.
export GTK_CSD=1

exec qtile start
