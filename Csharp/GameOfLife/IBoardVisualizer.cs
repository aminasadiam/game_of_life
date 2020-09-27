﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace GameOfLife
{
    public interface IBoardVisualizer
    {
        void DisplayCurrentStateOfBoard();
        void PlayGame();
    }
}
