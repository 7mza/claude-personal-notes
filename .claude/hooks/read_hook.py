#!/usr/bin/env python3
import json
import sys


def main():
    data = json.load(sys.stdin)
    path = data.get("tool_input", {}).get("file_path", "")

    if "do_not_read.txt" in path:
        print(
            json.dumps(
                {
                    "hookSpecificOutput": {
                        "hookEventName": "PreToolUse",
                        "permissionDecision": "deny",
                        "permissionDecisionReason": "la2777 !!",
                    }
                }
            )
        )
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
