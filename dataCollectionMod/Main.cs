using MelonLoader;
using UnityEngine;
using Assets.Scripts.Utils;
using Assets.Scripts.Unity.UI_New.InGame;

namespace paragonLog {

    public class Main : MelonMod {
        public override void OnUpdate() {
            base.OnUpdate();
            
            if (Input.GetKeyDown(KeyCode.Alpha8)) {
                foreach (var tower in InGame.instance.bridge.GetAllTowers()) {
                    if (tower.Def.isParagon) {
                        FileIOUtil.LogToFile("../../../../Documents/btd6/paragons/DartParagon" + tower.GetParagonDegreeMutator().degree + ".json", tower.Def);
                    }
                }
            }
        }
    }
}