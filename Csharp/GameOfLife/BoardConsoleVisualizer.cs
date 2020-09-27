using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace GameOfLife
{
    class BoardConsoleVisualizer : Board, IBoardVisualizer
    {
        public int AreaSize { get; set; }

        public int TimeSleep;

        public bool DisplayCurrentCoordinates;

        public BoardConsoleVisualizer(int? areaSize = null, int timeSleep = 250, bool displayCurrentCoordinates = false) 
        {
            if(areaSize == null)
                AreaSize = 5;  
            else
                AreaSize = (int)areaSize;

            if (timeSleep > 0)
                TimeSleep = timeSleep;
            else
                throw new ArgumentException("timeSleep must be bigger then zero.");

            DisplayCurrentCoordinates = displayCurrentCoordinates;
        }

      
        public void PlayGame()
        {
            // board after set all cells
            DisplayCurrentStateOfBoard();

            if (DisplayCurrentCoordinates)
                PrintCurrentStateCoordinates();

            Thread.Sleep(TimeSleep);
            while (true)
            {
                //Console.Clear();
                Console.SetCursorPosition(1, 0);

                NextState();
                DisplayCurrentStateOfBoard();

                if (DisplayCurrentCoordinates)
                    PrintCurrentStateCoordinates();

                Thread.Sleep(TimeSleep);
            }
        }
       
        public void DisplayCurrentStateOfBoard()
        {
            Console.WriteLine();

            for (int i = (int)-AreaSize; i < AreaSize * 2; i++)
            {
                for (int j = (int)-AreaSize * 4; j < AreaSize * 4; j++)
                {
                    if (IsCellExist(j, i))
                    {
                        Console.Write("+");
                    }
                    else
                    {
                        Console.Write(" ");
                    }
                }
                Console.WriteLine();
            }

            // Using PadLeft is helping when we rewrite on the console buffor.
            // (reason of troubles: Console.SetCursorPosition(1, 0) in PlayGame method)
            // PadLeft rescue us from different number of signs displaying on screen.
            Console.WriteLine("Cells on board: " + Convert.ToString(_currentState.Count).PadLeft(10, '0') + "\n");
        }


        public void PrintCurrentStateCoordinates()
        {
            Console.WriteLine();

            foreach (Cell cell in _currentState)
            {
                Console.WriteLine("X: " + cell.X + ", Y: " + cell.Y);
            }

            // Why use PadLeft was described in PrintCurrentBoard method.
            Console.WriteLine("Cells on board: " + Convert.ToString(_currentState.Count).PadLeft(10, '0') + "\n");
        }
    }
}
